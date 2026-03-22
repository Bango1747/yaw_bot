import argparse
import math


def compute_t_deg(a_deg: float, b_deg: float) -> float:
    """Compute equivalent knee angle t from branch hip angle a and mapped hip angle b.

    All inputs/outputs are in degrees.
    """
    a_rad = math.radians(a_deg)
    b_rad = math.radians(b_deg)
    x = 60.0 * (math.cos(b_rad) - math.cos(a_rad))
    y = 60.0 * (math.sin(b_rad) + math.sin(a_rad)) + 45.0
    chord = math.sqrt(x * x + y * y)
    inner_angle_deg = math.degrees(math.atan2(y, x))
    knee_triangle_angle_deg = math.degrees(math.acos(max(-1.0, min(1.0, -chord / 200.0))))
    return -180.0 + a_deg + inner_angle_deg + knee_triangle_angle_deg


def main():
    parser = argparse.ArgumentParser(description="Compute knee angle t from branch hip a and mapped hip b.")
    parser.add_argument("a", type=float, help="Branch hip angle a in degrees.")
    parser.add_argument("b", type=float, help="Mapped hip angle b in degrees.")
    args = parser.parse_args()

    t_deg = compute_t_deg(args.a, args.b)
    print(f"a = {args.a:.6f} deg")
    print(f"b = {args.b:.6f} deg")
    print(f"t = {t_deg:.6f} deg")


if __name__ == "__main__":
    main()
