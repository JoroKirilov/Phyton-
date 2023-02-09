from datetime import datetime, date
from decimal import Decimal
from unittest import *


def sum_two_numbers(a, b):
    return a + b

class SimpleFunction(TestCase):
    _todat = datetime.now().date()
    def test_sum_two_numbers(self):
        test_cases = [
            ((4, 5), 9),
        ]

        for (a, b), result in test_cases:
            with self.subTest(result=result):
                self.assertEqual(sum_two_numbers(a, b), result)

        self.assertRaises(TypeError, lambda: sum_two_numbers('4', 5))
        self.assertRaises(TypeError, lambda: sum_two_numbers(None, 6))


    @skipUnless(_todat >= date(2023, 11, 11), "not ready yet")
    def test_non_function(self):
        self.assertEqual(sum_three_numbers(4, 5, 4), 13)