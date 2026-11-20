from collections import Counter
from typing import Any, Dict, List, Sequence

def _ensure_not_empty(data: Sequence[float]) -> None: 
    if not data: 
        raise ValueError("Ряд пуст: расчёт статистики невозможен") 

def mean(data: Sequence[float]) -> float: 
    """Среднее арифметическое.""" 
    _ensure_not_empty(data) 
    return sum(data) / len(data) 

def median(data: Sequence[float]) -> float: 
    """Медиана (устойчива к выбросам).""" 
    _ensure_not_empty(data) 
    s = sorted(data) 
    k = len(s) // 2 
    if len(s) % 2: 
        return float(s[k]) 
    return (s[k - 1] + s[k]) / 2.0 

def spread(data: Sequence[float]) -> float: 
    """Размах ряда: max - min.""" 
    _ensure_not_empty(data) 
    return float(max(data) - min(data)) 

def mode(data: Sequence[float]) -> List[float]:
    """Мода ряда через Counter. При нескольких модах возвращает отсортированный список."""
    _ensure_not_empty(data)
    counts = Counter(data)
    max_freq = max(counts.values())
    return sorted(float(val) for val, freq in counts.items() if freq == max_freq)

def summarize(data: Sequence[float]) -> Dict[str, Any]:
    """Сводный отчёт: count, mean, median, spread, mode, min, max."""
    _ensure_not_empty(data)
    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "spread": spread(data),
        "mode": mode(data),
        "min": float(min(data)),
        "max": float(max(data)),
    }

