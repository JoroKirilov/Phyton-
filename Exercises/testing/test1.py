import unittest

class SimpleTest(unittest.TestCase):
    def test_upper(self):
        input_str = 'foo'.upper()
        result = 'FOo'
        self.assertEqual(input_str, result, "This is simple test")
