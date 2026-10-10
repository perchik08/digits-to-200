"""Insert +, -, or nothing between 9876543210 to reach the target."""

DIGITS = "9876543210"


def solve(target: int = 200) -> list[str]:
    """Return every matching expression, without an equals sign."""
    solutions: list[str] = []

    def search(position: int, total: int, expression: str) -> None:
        if position == len(DIGITS):
            if total == target:
                solutions.append(expression)
            return

        # Each consecutive group of digits becomes the next number.
        for end in range(position + 1, len(DIGITS) + 1):
            token = DIGITS[position:end]
            number = int(token)

            if position == 0:
                # The task allows operators only BETWEEN digits.
                search(end, number, token)
            else:
                search(end, total + number, f"{expression}+{token}")
                search(end, total - number, f"{expression}-{token}")

    search(0, 0, "")
    return solutions


if __name__ == "__main__":
    for solution in solve():
        print(f"{solution}=200")
