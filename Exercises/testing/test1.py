import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        input_str = 'foo'.upper()
        result = 'FOO'
        self.assertEqual(input_str, result, "This is simple test")

    def test_add_operation(self):
        a = 10
        b = 15
        exp_result = 25
        self.assertEqual(a + b, exp_result)


if __name__ == '__main__':
    unittest.main()
