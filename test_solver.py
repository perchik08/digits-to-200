"""Check the puzzle contract and completeness with an independent oracle."""

import re
import unittest
from itertools import product

from solver import solve


class SolverTests(unittest.TestCase):
    def test_includes_example_from_assignment(self):
        self.assertIn("98+76-5+43-2-10", solve())

    def test_every_solution_is_valid_and_unique(self):
        solutions = solve()
        self.assertTrue(solutions)
        self.assertEqual(len(solutions), len(set(solutions)))
        for expression in solutions:
            with self.subTest(expression=expression):
                self.assertRegex(expression, r"^9[0-9+\-]*0$")
                self.assertEqual(re.sub(r"[+\-]", "", expression), "9876543210")
                self.assertEqual(sum(map(int, re.findall(r"[+\-]?\d+", expression))), 200)

    def test_finds_exactly_all_valid_combinations(self):
        # Independent approach: enumerate operators, then parse signed numbers.
        expected = set()
        for operators in product(("", "+", "-"), repeat=9):
            expression = "9" + "".join(
                operator + digit for operator, digit in zip(operators, "876543210")
            )
            if sum(map(int, re.findall(r"[+\-]?\d+", expression))) == 200:
                expected.add(expression)
        self.assertEqual(set(solve()), expected)

    def test_concatenation_and_unreachable_target(self):
        self.assertEqual(solve(9876543210), ["9876543210"])
        self.assertEqual(solve(9876543211), [])


if __name__ == "__main__":
    unittest.main()
