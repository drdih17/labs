from validation import input_length, input_width, input_thickness, input_quantity
from menu import show_menu, select_mode, mode_name
from operations import get_mass,  thickness_class


def main() -> None:
    """Main scenario."""
    print("=== Mass and thickness class evaluation ===")

    while True:
        show_menu()
        p = select_mode()
        if p is None:
            print("Work completed.")
            break

        l = input_length()
        w = input_width()
        t = input_thickness()
        q = input_quantity()


        m = get_mass(l, w, t, q, p)
        cls = thickness_class(t)

        print("\n===Results===")
        print(f"Material:          {mode_name(p)} (p = {p})")
        print(f"Mass:              {m:.2f} kg")
        print(f"Thickness class:   {cls}")
        print("\n")


if __name__ == "__main__":
    main()
