import sys


def calculate(left: float, operator: str, right: float) -> float:
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ValueError("Cannot divide by zero")
        return left / right
    raise ValueError(f"Unsupported operator: {operator}")


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <number> <operator> <number>")
        return 1

    try:
        left = float(sys.argv[1])
        operator = sys.argv[2]
        right = float(sys.argv[3])
        result = calculate(left, operator, right)
    except ValueError as error:
        print(error)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
