from unittest import TestCase

from quadratic import solve


class SolveTests(TestCase):
    def test_real_roots(self) -> None:
        cases = (
            ((1, -3, 2), (1.0, 2.0)),
            ((1, 0, 1), ()),
            ((0, 2, -4), (2.0,)),
            ((0, 0, 1), ()),
            ((0, 0, 0), None),
            ((0.5, -1.75, 1.5), (1.5, 2.0)),
        )
        for coefficients, expected in cases:
            with self.subTest(coefficients=coefficients):
                self.assertEqual(solve(*coefficients), expected)
