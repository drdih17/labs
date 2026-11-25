"""Интеграционные тесты CLI через subprocess.""" 
import subprocess 
import sys 
from pathlib import Path 
import pytest 
ROOT = Path(__file__).resolve().parent.parent 
MAIN = ROOT / "main.py" 
  
 
  
def run_cli(*args: str) -> subprocess.CompletedProcess: 
    """Запустить main.py с аргументами и вернуть результат.""" 
    return subprocess.run( 
 
        [sys.executable, str(MAIN), *args], 
        capture_output=True, 
        text=True, 
        cwd=ROOT, 
        timeout=30, 
    ) 
  
  
class TestCLI: 
    def test_runs_successfully(self): 
        r = run_cli("--kind", "sine", "--n", "20", "--window", "3", "--seed", "1") 
        assert r.returncode == 0, r.stderr 
        assert "Среднее" in r.stdout 
        assert "SMA" in r.stdout 
  
    def test_all_kinds_work(self): 
        for kind in ("random", "sine", "trend", "gauss"): 
            r = run_cli("--kind", kind, "--n", "10") 
            assert r.returncode == 0, f"{kind}: {r.stderr}" 
  
    def test_defaults_work(self): 
        r = run_cli() 
        assert r.returncode == 0 
  
    def test_invalid_kind_fails(self): 
        r = run_cli("--kind", "foo") 
        assert r.returncode != 0 
  
    def test_invalid_n_fails_gracefully(self): 
        r = run_cli("--n", "-5") 
        assert r.returncode == 1 
        assert "Ошибка" in r.stderr 
  
    def test_benchmark_flag(self): 
        r = run_cli("--kind", "random", "--n", "50", "--window", "5", "--benchmark") 
        assert r.returncode == 0, r.stderr 
        assert "list" in r.stdout and "deque" in r.stdout 
  
  
class TestCLIIO: 
    """Тесты расширения --save / --load.""" 
  
    def test_save_then_load(self, tmp_path: Path): 
        pytest.importorskip("num_series.io_json") 
        path = tmp_path / "series.json" 
        r1 = run_cli("--kind", "sine", "--n", "10", "--save", str(path)) 
        assert r1.returncode == 0, r1.stderr 
        assert path.exists() 
  
        r2 = run_cli("--load", str(path), "--window", "3") 
        assert r2.returncode == 0, r2.stderr 
  
    def test_load_missing_file_fails(self, tmp_path: Path): 
  
        pytest.importorskip("num_series.io_json") 
        r = run_cli("--load", str(tmp_path / "nope.json")) 
        assert r.returncode == 1 


class TestCLIVariant2:
    """Интеграционные проверки варианта 2: gauss, мода, WMA."""

    def test_gauss_kind_prints_mode_and_wma(self):
        r = run_cli(
            "--kind", "gauss", "--n", "50", "--seed", "42", "--window", "5"
        )
        assert r.returncode == 0, r.stderr
        assert "gauss" in r.stdout
        assert "Мода" in r.stdout
        assert "WMA" in r.stdout

    def test_gauss_save_then_load(self, tmp_path: Path):
        path = tmp_path / "gauss.json"
        r1 = run_cli(
            "--kind", "gauss", "--n", "30", "--seed", "7", "--save", str(path)
        )
        assert r1.returncode == 0, r1.stderr
        assert path.exists()

        r2 = run_cli("--load", str(path), "--window", "5")
        assert r2.returncode == 0, r2.stderr
        assert "Мода" in r2.stdout
        assert "WMA" in r2.stdout

    def test_constant_series_edge_case(self, tmp_path: Path):
        path = tmp_path / "constant.txt"
        path.write_text("\n".join(["50"] * 20), encoding="utf-8")

        r = run_cli("--load", str(path), "--window", "5")
        assert r.returncode == 0, r.stderr
        assert "Мода" in r.stdout
        assert "50.0000" in r.stdout
        assert "0.0000" in r.stdout  # размах (max - min) == 0 при СКО = 0

    @pytest.mark.parametrize("args", [
        ("--window", "0"),
        ("--window", "-3"),
        ("--alpha", "0"),
        ("--alpha", "1.5"),
        ("--n", "0"),
        ("--n", "5", "--window", "10"),
    ])
    def test_invalid_parameters_return_1(self, args):
        r = run_cli(*args)
        assert r.returncode == 1, r.stdout + r.stderr
        assert "Ошибка" in r.stderr