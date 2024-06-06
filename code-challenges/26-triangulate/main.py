from enum import Enum


class TriangleType(Enum):
    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"
    RIGHT_ANGLED = "right-angled"


def equal_ish(a: float, b: float) -> bool:
    return abs(a - b) < 0.0001


def check_triangle_type(
    side_a: float, side_b: float, side_c: float
) -> TriangleType | None:
    # TODO: Check if it's a valid triangle

    if equal_ish(side_a**2 + side_b**2, side_c**2):
        return TriangleType.RIGHT_ANGLED
    if equal_ish(side_a, side_b) and equal_ish(side_b, side_c):
        return TriangleType.EQUILATERAL
    if (
        equal_ish(side_a, side_b)
        or equal_ish(side_b, side_c)
        or equal_ish(side_a, side_c)
    ):
        return TriangleType.ISOSCELES
    return TriangleType.SCALENE


def check_triangle_demo(sides: tuple[float, float, float]):
    result = check_triangle_type(*sides)
    if result is None:
        print(f"Triangle {sides} is not a valid triangle")
        return
    print(f"Triangle {sides} is {result.value.capitalize()}")
