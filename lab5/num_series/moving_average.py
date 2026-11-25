import time 
from collections import deque 
from typing import List, Sequence 

def check_window(window: int, n: int) -> None:
    if isinstance(window, bool) or not isinstance(window, int):
        raise ValueError("Размер окна должен быть целым числом")
    if window < 1:
        raise ValueError("Размер окна должен быть >= 1")
    if window > n:
        raise ValueError("Размер окна больше длины ряда")
    

def simple_moving_average(data: list[float], window: int) -> float:
    n = len(data)

    check_window(window, n)

    if n == 0:
        return []

    running_sum = sum(data[:window])
    result = [running_sum / window]


    for i in  range(window, n):
        running_sum += data[i] - data[i - window]
        result.append(running_sum / window)

    return result


def exponential_moving_average(
    data: list[float], 
    alpha: float
) -> list[float]:
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")

    if isinstance(alpha, bool) or not (0 < alpha <= 1):
        raise ValueError("alpha must be in (0 ; 1]")

    ema = [data[0]]
    for i in range(1, len(data)):
        ema.append(alpha * data[i] + (1 - alpha) * ema[i - 1])

    return ema

def centered_moving_average(
    data: Sequence[float],
    window: int,
) -> List[float]:
    """Центрированное MA на базе list: окно нечётное, результат выровнен по центру."""
    if not data:
        raise ValueError("Ряд пуст: расчёт CMA невозможен")
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"Центрированное MA требует нечётного window, получено: {window}"
        )

    n = len(data)
    running = sum(data[:window])
    result: List[float] = [running / window]

    for i in range(window, n):
        running += data[i] - data[i - window]
        result.append(running / window)

    return result

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]: 
    """SMA с использованием deque (двусторонней очереди).""" 
    check_window(window, len(data)) 
    result = [] 
    d = deque() 
    running_sum = 0.0 
    for x in data: 
        d.append(x) 
        running_sum += x 
        if len(d) > window: 
            running_sum -= d.popleft() 
        if len(d) == window: 
            result.append(running_sum / window) 
    return result 

def benchmark_moving_average(data: Sequence[float], window: int, repeats: int = 1000) -> dict: 
    """ 
    Замеряет среднее время выполнения SMA для реализаций на list и deque. 
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах). 
    """ 
    # Проверка корректности окна (выбросит ValueError при необходимости) 
    check_window(window, len(data)) 
    # Замер для list-реализации (существующая simple_moving_average) 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average(data, window) 
    t_list = (time.perf_counter() - t0) / repeats 
    # Замер для deque-реализации 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average_deque(data, window) 
    t_deque = (time.perf_counter() - t0) / repeats 
    return {"list": t_list, "deque": t_deque}

def weighted_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Взвешенная скользящая средняя (WMA) c линейными весами 1..window."""
    if not data:
        raise ValueError("Ряд пуст: расчёт WMA невозможен")
    check_window(window, len(data))

    weight_sum = window * (window + 1) / 2.0
    result: List[float] = []

    for i in range(len(data) - window + 1):
        weighted_total = sum(
            (w + 1) * data[i + w] for w in range(window)
        )
        result.append(weighted_total / weight_sum)

    return result
