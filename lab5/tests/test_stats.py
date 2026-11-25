"""Тесты модуля num_series.stats.""" 
import statistics 
import pytest 
from num_series.stats import mean, median, spread, mode, summarize 
  
  
class TestMean: 
    @pytest.mark.parametrize("data,expected", [ 
        ([1], 1.0), 
        ([1, 2, 3], 2.0), 
        ([1, 2, 3, 4], 2.5), 
        ([-5, 5], 0.0), 
        ([0, 0, 0], 0.0), 
    ]) 
    def test_basic(self, data, expected): 
        assert mean(data) == pytest.approx(expected) 
  
    def test_empty_raises(self): 
        with pytest.raises(ValueError, match="пуст"): 
            mean([]) 
  
    def test_floats(self): 
        assert mean([0.1, 0.2, 0.3]) == pytest.approx(0.2) 
  
  
class TestMedian: 
    @pytest.mark.parametrize("data,expected", [ 
        ([1], 1), 
        ([1, 2, 3], 2), 
        ([3, 1, 2], 2), 
        ([1, 2, 3, 4], 2.5), 
        ([4, 1, 3, 2], 2.5), 
        ([-3, -1, -2], -2), 
        ([0, 0, 0, 0], 0), 
    ]) 
    def test_basic(self, data, expected): 
        assert median(data) == pytest.approx(expected) 
  
    def test_empty_raises(self): 
        with pytest.raises(ValueError): 
            median([])  
  
    def test_resistant_to_outlier(self): 
        clean = [1, 2, 3, 4, 5] 
        with_outlier = [1, 2, 3, 4, 1000] 
        assert median(clean) == 3 
        assert median(with_outlier) == 3 
  
  
class TestSpread: 
    @pytest.mark.parametrize("data,expected", [ 
        ([5], 0), 
        ([1, 2, 3], 2), 
        ([-10, 10], 20), 
        ([0, 0, 0], 0), 
    ]) 
    def test_basic(self, data, expected): 
        assert spread(data) == expected 
  
    def test_empty_raises(self): 
        with pytest.raises(ValueError): 
            spread([]) 
  
  
class TestSummarize: 
    def test_keys(self): 
        s = summarize([1, 2, 3, 4, 5]) 
        assert set(s) == {"count", "mean", "median", "spread", "mode", "min", "max"} 
  
    def test_values(self): 
        s = summarize([1, 2, 3, 4, 5]) 
        assert s["count"] == 5 
        assert s["mean"] == pytest.approx(3.0) 
        assert s["median"] == 3 
        assert s["spread"] == 4 
        assert s["mode"] == [1.0, 2.0, 3.0, 4.0, 5.0] 
        assert s["min"] == 1 
        assert s["max"] == 5 
   
    def test_empty_raises(self): 
        with pytest.raises(ValueError): 
            summarize([]) 


class TestMode:
    """Вариант 2: мода через collections.Counter."""

    @pytest.mark.parametrize("data,expected", [
        ([1, 2, 2, 3], [2.0]),
        ([4, 4, 1, 1, 2], [1.0, 4.0]),
        ([7, 7, 7], [7.0]),
        ([3, 1, 2], [1.0, 2.0, 3.0]),
        ([1.5, 2.5, 1.5, 2.5, 3.5], [1.5, 2.5]),
        ([-1, -1, 0, 2], [-1.0]),
    ])
    def test_basic(self, data, expected):
        assert mode(data) == expected

    def test_returns_list_even_for_single_mode(self):
        result = mode([5, 5, 1])
        assert isinstance(result, list)
        assert result == [5.0]

    def test_empty_raises(self):
        with pytest.raises(ValueError, match="пуст"):
            mode([])


class TestConstantSeriesEdgeCase:

    def test_zero_stdev_and_stats(self):
        data = [50.0] * 100
        assert statistics.pstdev(data) == 0.0
        assert statistics.stdev(data) == 0.0

        s = summarize(data)
        assert s["count"] == 100
        assert s["mean"] == pytest.approx(50.0)
        assert s["median"] == pytest.approx(50.0)
        assert s["spread"] == 0.0
        assert s["mode"] == [50.0]
        assert s["min"] == s["max"] == 50.0