import math

def check_point_position(x: float, y: float) -> str:
    epsilon = 1e-9

    r = 3.5

    xc, yc = 3.5, -3.5
    r = 3.5
    dist_sq = (x - xc) ** 2 + (y - yc) ** 2
    r_sq = r ** 2

    in_rect = (0 <= x <= 14) and (-7 <= y <= 0)
    on_rect_boundary = (
        (math.isclose(x, 0, abs_tol=epsilon) or math.isclose(x, 14, abs_tol=epsilon)) and (-7 <= y <= 0)
    ) or ( 
        math.isclose(y, 0, abs_tol=epsilon) or math.isclose(y, -7, abs_tol=epsilon) and (0 <= x <= 14)
    )
    
    on_circle_boundary = math.isclose(dist_sq, r_sq, abs_tol=epsilon)
    inside_circle = dist_sq < r_sq - epsilon

    if not in_rect: 
        return "Out of bounds"

    if on_circle_boundary or on_rect_boundary:
        return "On the edge of the bound"

    if inside_circle:
        return "Out of bounds"

    return "Inside of the figure"


def main():
    try:
        x = float(input("X: "))
        y = float(input("Y: "))
        result = check_point_position(x, y)
        print(f"Result: {result}")
    except ValueError:
        print("X or Y not a number")

main()