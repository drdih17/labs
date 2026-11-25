"""Тесты модуля num_series.generator.""" 
import statistics 
import pytest 
from num_series.generator import ( 
    random_series, 
    sine_series, 
    trend_series, 
    _validate_n, 
    gauss_series
) 
class TestValidateN: 
    """Границы и типы входного параметра n.""" 
  
    @pytest.mark.parametrize("n", [1, 5, 100, 1000]) 
    def test_positive_int_passes(self, n): 
        _validate_n(n) 
  
    @pytest.mark.parametrize("n", [0, -1, -100]) 
    def test_zero_and_negative_rejected(self, n): 
        with pytest.raises(ValueError, match="положительным целым"): 
            _validate_n(n) 
  
    @pytest.mark.parametrize("n", [3.5, -0.1, 1.0000001]) 
    def test_non_integer_float_rejected(self, n): 
        with pytest.raises(ValueError, match="положительным целым"): 
            _validate_n(n) 
  
    @pytest.mark.parametrize("n", ["5", "abc", None, [5], {"n": 5}]) 
    def test_bad_types_rejected(self, n): 
        with pytest.raises(ValueError, match="положительным целым"): 
            _validate_n(n) 
  
    def test_error_message_contains_repr_and_cause(self): 
        with pytest.raises(ValueError) as exc_info: 
            _validate_n("abc") 
        msg = str(exc_info.value) 
        assert "'abc'" in msg 
        assert "причина" in msg 
  
    def test_float_integral_passes(self):  
        _validate_n(3.0) 
  
  
class TestRandomSeries: 
    def test_length(self): 
        assert len(random_series(10, seed=1)) == 10 
  
    def test_reproducible_with_seed(self): 
        assert random_series(20, seed=42) == random_series(20, seed=42) 
  
    def test_different_seeds_differ(self): 
        assert random_series(20, seed=1) != random_series(20, seed=2) 
  
    def test_within_bounds(self): 
        data = random_series(100, low=-5, high=5, seed=0) 
        assert all(-5 <= x <= 5 for x in data) 
  
    def test_low_ge_high_raises(self): 
        with pytest.raises(ValueError, match="low должно быть меньше high"): 
            random_series(5, low=10, high=5) 
  
    def test_invalid_n_raises(self): 
        with pytest.raises(ValueError): 
            random_series(0) 
  
class TestSineSeries: 
    def test_length(self): 
        assert len(sine_series(30, seed=0)) == 30 
  
    def test_reproducible(self): 
        assert sine_series(30, noise=0.5, seed=7) == sine_series(30, noise=0.5, seed=7) 
  
    def test_zero_noise_is_deterministic_without_seed(self): 
        a = sine_series(20, noise=0.0, seed=1) 
        b = sine_series(20, noise=0.0, seed=999) 
        assert a == b 
  
    def test_amplitude_bounds_without_noise(self): 
        data = sine_series(100, amplitude=2.0, noise=0.0) 
        assert all(-2.0 - 1e-9 <= x <= 2.0 + 1e-9 for x in data) 
  
  
class TestTrendSeries: 
    def test_linear_without_noise(self): 
        data = trend_series(5, start=0, step=2.0, noise=0.0) 
        assert data == [0.0, 2.0, 4.0, 6.0, 8.0] 
  
    def test_length(self): 
        assert len(trend_series(15, seed=0)) == 15 
  
    def test_reproducible(self): 
        assert trend_series(10, noise=0.5, seed=3) == trend_series(10, noise=0.5, seed=3) 

class TestGaussSeries:

    def test_default_length_is_500(self):
        assert len(gauss_series(seed=1)) == 500

    def test_length(self):
        assert len(gauss_series(30)) == 30

    def test_elements_are_float(self):
        data = gauss_series(50, mu=50, sigma=10, seed=1)
        assert all(isinstance(x, float) for x in data)

    def test_reproducible(self):
        assert gauss_series(30, 50, 10, 10) == gauss_series(30, 50, 10, 10)

    def test_different_seeds_differ(self):
        assert gauss_series(30, 50, 10, 1) != gauss_series(30, 50, 10, 2)

    def test_sample_mean_and_stdev_close_to_parameters(self):
        data = gauss_series(500, mu=50, sigma=10, seed=42)
        assert statistics.mean(data) == pytest.approx(50.0, abs=1.5)
        assert statistics.pstdev(data) == pytest.approx(10.0, abs=1.0)

    def test_values_inside_wide_sigma_range(self):
        data = gauss_series(500, mu=50, sigma=10, seed=42)
        assert all(50 - 6 * 10 <= x <= 50 + 6 * 10 for x in data)

    def test_sigma_zero_gives_constant_series(self):
        data = gauss_series(50, mu=50, sigma=0, seed=42)
        assert data == [50.0] * 50
        assert statistics.pstdev(data) == 0.0

    def test_negative_sigma_raises(self):
        with pytest.raises(ValueError):
            gauss_series(10, mu=50, sigma=-1)

    def test_invalid_n_raises(self):
        with pytest.raises(ValueError):
            gauss_series(0)

