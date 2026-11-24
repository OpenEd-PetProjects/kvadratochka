from math import sqrt


def solve(a: float, b: float, c: float) -> tuple[float, ...] | None:
    """Return the real roots, or None if every real number is a solution."""
    if a == 0:
        if b == 0:
            return None if c == 0 else ()
        return (-c / b,)

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return ()

    root = sqrt(discriminant)
    denominator = 2 * a
    return ((-b - root) / denominator, (-b + root) / denominator)


if __name__ == "__main__":
    roots = solve(float(input("a: ")), float(input("b: ")), float(input("c: ")))
    if roots is None:
        print("Infinitely many solutions.")
    elif roots:
        print("Real roots:", ", ".join(map(str, roots)))
    else:
        print("No real roots.")
