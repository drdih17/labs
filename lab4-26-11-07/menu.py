from connstans import STEEL, ALUMINUM, COPPER
import logger
import validation
from typing import Annotated


def show_menu() -> None:
    """Show available materials."""
    print("\n Choose material to work with:")
    print("  1 — Steel         (p = 7850)")
    print("  2 — Aluminum      (p = 2700)")
    print("  3 — Copper        (p = 8900)")
    print("  0 — Exit")


def select_mode() -> float | None:
    """
    Ask for the input with materiak number

    Returns None if typed 0.
    """
    while True:
        choice = validation.input_number_int("Input material number (from 0 to 3): ", 0, 3)
        print(choice)
        match choice:
            case 1:
                return STEEL
            case 2:
                return ALUMINUM
            case 3:
                return COPPER
            case 0:
                return None
            case _:
                print("Error: wrong material number. Try again")
                logger.log_error("Wrong material number")


def mode_name(
    p: Annotated[float, "Material density"]
    ) -> str:
    """Return material name by P."""
    match p:
        case 7850:
            return "Steel"
        case 2700:
            return "Aluminum"
        case 8900:
            return "Copper"
        case _:
            logger.log_error("Unknown material")
            return "Unknown material"