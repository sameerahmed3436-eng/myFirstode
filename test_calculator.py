import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_addition(self) -> None:
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self) -> None:
        self.assertEqual(calculate(5, "-", 3), 2)

    def test_multiplication(self) -> None:
        self.assertEqual(calculate(4, "*", 3), 12)

    def test_division(self) -> None:
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_division_by_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            calculate(8, "/", 0)

    def test_unknown_operator_raises(self) -> None:
        with self.assertRaises(ValueError):
            calculate(8, "%", 2)


if __name__ == "__main__":
    unittest.main()
