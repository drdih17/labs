from connstans import L_MIN, L_MAX, W_MIN, W_MAX, T_MIN, T_MAX, Q_MIN, Q_MAX
from logger import log_error
from typing import Annotated


def validate_range(
    value: float, 
    low: Annotated[float, "Lowest boundry"], 
    high: Annotated[float, "Highest boundry"]
    ) -> tuple[bool, str]:
    """
    Checks if value in range [low, high].
    :return: (True, "") or (False, сообщение)
    """
    if value < low:
        return False, f"Error: Value ({value}) is lower than minumum value ({low})."
    elif value > high:
        return False, f"Error: Value ({value}) is higher than maximum value ({high})."
    else:
        return True, ""


def input_number(
    prompt: Annotated[str, "Input message"], 
    low: Annotated[float, "Lowest boundry"], 
    high: Annotated[float, "Highest boundry"]
    ) -> float:
    """
    Ask for a float number in cycle, while correct one is not inputed.
    Checks for type (float).
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Error: input is not a number ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Try again.")
        log_error(msg)

def input_number_int(
    prompt: Annotated[str, "Input message"], 
    low: Annotated[float, "Lowest boundry"], 
    high: Annotated[float, "Highest boundry"]
    ) -> int:
    """
    Ask for an integer in cycle, while correct one is not inputed.
    Checks for type (integer).
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Error: input is not a number ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Try again.")
        log_error(msg)


def input_length() -> float:
    '''
    Ask for a number and make sure it is float and in the boundries
    '''
    return input_number(
        "INPUT LENGTH: ",
        L_MIN, L_MAX,
    )


def input_width() -> float:
    '''
    Ask for a number and make sure it is float and in the boundries
    '''
    return input_number(
        "INPUT WIDTH: ",
        W_MIN, W_MAX,
    )

def input_thickness() -> float:
    '''
    Ask for a number and make sure it is float and in the boundries
    '''
    return input_number(
        "INPUT THICKNESS: ",
        T_MIN, T_MAX,
    )

def input_quantity() -> int:
    '''
    Ask for a number and make sure it is integer and in the boundries
    '''
    return input_number_int(
        "INPUT QUANTITY: ",
        Q_MIN, Q_MAX,
    )
