from decimal import Decimal
from unittest import TestCase

def sum_two_numbers(a, b):
    return a + b

class SimpleFunction(TestCase):
    def test_sum_two_numbers(self):
        test_cases = [
            ((4, 5), 9),
            # (('4', 5), 9),
            # ((None, 5), 9),
            # ((Decimal(5), 5.1), 10.1)
        ]

        for (a, b), result in test_cases:
            with self.subTest(result=result):
                self.assertEqual(sum_two_numbers(a, b), result)

        self.assertRaises(TypeError, lambda: sum_two_numbers('4', 5))
        self.assertRaises(TypeError, lambda: sum_two_numbers(None, 6))
