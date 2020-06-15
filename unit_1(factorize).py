import unittest


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        """
        The function throws TypeError exception
        if recieves 'float' or 'str' args:
        'string', 1.5
        """
        cases = ('string', 1.5)
        for x in cases:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        """
        Checks 'factorize' for throwing ValueError
        if accepts negative number: -1, -10, -100
        """
        cases = (-1, -10, -100)
        for x in cases:
            with self.subTest(case=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        """
        The func must return tuples for numbers 0 and 1:
        0 -> (0,), 1 -> (1,)
        """
        cases = ((0, (0,)), (1, (1,)))
        for x, expected in cases:
            with self.subTest(case=x):
                b = factorize(x)
                self.assertEqual(expected, b)

    def test_simple_numbers(self):
        """
        For primes, returns a tuple with one given prime number.
        3 -> (3,), 13 -> (13,), 29 -> (29,)
        """
        cases = ((3, (3,)), (13, (13,)), (29, (29,)))
        for x, expected in cases:
            with self.subTest(case=x):
                b = factorize(x)
                self.assertEqual(expected, b)

    def test_two_simple_multipliers(self):
        """
        Checks cases when numbers are passed for which
        the factorize function returns a tuple with two elements
        6 -> (2, 3), 26 -> (2, 13), 121 -> (11, 11)
        """
        cases = ((6, (2, 3)), (26, (2, 13)), (121, (11, 11)))
        for x, expected in cases:
            with self.subTest(case=x):
                b = factorize(x)
                self.assertEqual(expected, b)

    def test_many_multipliers(self):
        """
        Checks cases when numbers are passed for which the
        factorize function returns a tuple with numbers of elements
        greater than 2
        1001 -> (7, 11, 13), 9699690 -> (2, 3, 5, 7, 11, 13, 17, 19)
        """
        cases = ((1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)))
        for x, expected in cases:
            with self.subTest(case=x):
                b = factorize(x)
                self.assertEqual(expected, b)

