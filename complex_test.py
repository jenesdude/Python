from complex import Complex
from math import sqrt
import unittest


class ComplexTestCase(unittest.TestCase):
    def testStringRepresentation(self):
        self.assertEqual(str(Complex(1, 1)), '(1+1j)')
        self.assertEqual(str(Complex(1, -1)), '(1-1j)')

    def testComponentOfComplex(self):
        self.assertEqual(Complex(1, 1).real, 1)
        self.assertEqual(Complex(1, 1).imag, 1)
        self.assertEqual(Complex(2, 0).magnitude, 2.0)
        self.assertEqual(Complex(1, 1).magnitude, sqrt(2))
        self.assertEqual(Complex(1, 1).conjugate, Complex(1, -1))

    def testEqualityInequality(self):
        self.assertEqual(Complex(1, 1) == Complex(1, 1), True)
        self.assertEqual(Complex(1, 1) == Complex(1, 2), False)
        self.assertEqual(Complex(1, 1) != Complex(1, 1), False)
        self.assertEqual(Complex(1, 1) != Complex(1, 2), True)

    def testAddition(self):
        self.assertEqual(Complex(1, 1) + Complex(1, 1), Complex(2, 2))
        self.assertEqual(Complex(2.5, 4) + Complex(4, 2.5), Complex(6.5, 6.5))

    def testMultiplexing(self):
        self.assertEqual(Complex(0, 1) * Complex(0, 1), Complex(-1, 0))
        self.assertEqual(Complex(1, 1) * Complex(2, 2), Complex(0, 4))
        self.assertEqual(Complex(2, 0) * Complex(3, 0), Complex(6, 0))

    def testExponentiation(self):
        self.assertEqual((Complex(1, 0) ** 2).real == 1 and (Complex(1, 0) ** 2).imag == 0, True)
        self.assertEqual((Complex(0, 1) ** 2).real == -1 and (Complex(0, 1) ** 2).imag == 0, True)
        self.assertEqual((Complex(1, 1) ** 2).real == 0 and (Complex(1, 1) ** 2).imag == 2, True)
        self.assertEqual(Complex(0, 1).int_pow(2).real == -1 and Complex(0, 1).int_pow(2).imag == 0, True)


# def test(got, expected):
#     """Test method
#
#     Allow to make simple checking-comfortable tests
#     """
#     if got == expected:
#         prefix = ' OK '
#     else:
#         prefix = '  X '
#     print('{0} got: {1:20} expected: {2}'.format(prefix, repr(got),
#                                                  repr(expected)))
#     return got == expected
#
#
# def success_test(*value):
#     """Function shows if test passed successfully or not
#
#     Really. It`s just part of comfortable to debugging interface
#     """
#     if value:
#         print('tests passed successfully')
#     else:
#         print('tests crushed')
#     print()
#
#
# def test_method():
#     """Just test_method()
#
#     Big count of test examples for complex numbers
#     """
#     print('string representation')
#     success_test(
#         test(str(Complex(1, 1)), '(1+1j)'),
#         test(str(Complex(1, -1)), '(1-1j)')
#         )
#
#     print('components of a complex number')
#     success_test(
#         test(Complex(1, 1).real, 1),
#         test(Complex(1, 1).imag, 1),
#         test(Complex(2, 0).magnitude, 2.0),
#         test(Complex(1, 1).magnitude, sqrt(2)),
#         test(Complex(1, 1).conjugate, Complex(1, -1))
#         )
#
#     print('equality and inequality')
#     success_test(
#         test(Complex(1, 1) == Complex(1, 1), True),
#         test(Complex(1, 1) == Complex(1, 2), False),
#         test(Complex(1, 1) != Complex(1, 1), False),
#         test(Complex(1, 1) != Complex(1, 2), True)
#         )
#
#     print('addition')
#     success_test(
#         test(Complex(1, 1) + Complex(1, 1) == Complex(2, 2), True),
#         test(Complex(2.5, 4) + Complex(4, 2.5) == Complex(6.5, 6.5), True)
#         )
#
#     print('multiplication')
#     success_test(
#         test(Complex(1, 1) * Complex(2, 2) == Complex(0, 4), True),
#         test(Complex(2, 0) * Complex(3, 0) == Complex(6, 0), True)
#         )
#
#     print('exponentiation')
#     success_test(test((Complex(1, 0) ** 2).real == 1 and
#                       (Complex(1, 0) ** 2).imag == 0, True),
#                  test((Complex(0, 1) ** 2).real == -1 and
#                       (Complex(0, 1) ** 2).imag == 0, True),
#                  test((Complex(1, 1) ** 2).real == 0 and
#                       (Complex(1, 1) ** 2).imag == 2, True),
#                  test((Complex(1, 1).int_pow(2)).real == 0 and
#                       (Complex(1, 1).int_pow(2)).imag == 2, True))
#     print('Test system made by Maxim Smagin')


if __name__ == "__main__":
    unittest.main()