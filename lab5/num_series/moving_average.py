def check_window(window:  int, n: int) -> None:
    is_window_alr = window >= 1 and window <= n

    if not is_window_alr:
        raise ValueError("smth wrng w/ window or n")

def simple_moving_average(data: list[float], window) -> float:
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
            return []

        if not (0 < alpha <= 1):
            raise ValueError("alpha must be in (0 ; 1]")

        ema = [data[0]]

        for i in range(1, len(data)):
            ema.append(alpha * data[i] + (1 - alpha) * ema[i - 1])

        return ema

