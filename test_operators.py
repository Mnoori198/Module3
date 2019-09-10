import unittest
from main import operators

class MyTestCase(unittest.TestCase):
    def test_Modulus(self):

        self.assertTrue(operators.modulus(5, 2), 1)

    def test_not_true(self):

        self.assertFalse(operators.not_true(2, 5))

    def test_is_true(self):

        self.assertTrue(operators.not_equal(2, 5))

    def test_less_than(self):

        self.assertTrue(operators.value_less_than(2, 5))

if __name__ == '__main__':
    unittest.main()
