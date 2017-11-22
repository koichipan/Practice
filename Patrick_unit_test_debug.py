import xmlrunner
import unittest


class Calculator:

    def mod(self, dividend, divisor):
        remainder = dividend % divisor
        quotient = (dividend - remainder) / divisor
        return quotient, remainder


'''
assertTrue(expr, msg=None)
assertFalse(expr, msg=None)
assertEqual(first, second, msg=None)
assertNotEqual(first, second, msg=None)
'''


class CalculatorTest(unittest.TestCase):
    def test_mod_with_remainder(self):
        cal = Calculator()
        self.assertEqual(cal.mod(5, 3), (1, 0))

    def test_mod_without_remainder(self):
        cal = Calculator()
        self.assertEqual(cal.mod(5, 3), (1, 2))

    def test_mod_divide_by_zero(self):
        cal = Calculator()
        self.assertEqual(cal.mod(5, 3), (1, 2))


if __name__ == '__main__':
    ''' suite = unittest.defaultTestLoader.loadTestsFromTestCase(CalculatorTest)
    unittest.TextTestRunner().run(suite) '''
    unittest.main()
