import unittest
from functions import *

class TestAddSub(unittest.TestCase):
    def setUp(self):
        self.a = 20
        self.b = 10

    def test_add(self):
        result = add(self.a, self.b)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = subtract(self.a, self.b)
        self.assertEqual(result, 10)


class TestMulDiv(unittest.TestCase):
    def setUp(self):
        self.a = 20
        self.b = 10

    def test_mul(self):
        result = multiply(self.a, self.b)
        self.assertEqual(result, 200)

    def test_div(self):
        result = divide(self.a, self.b)
        self.assertEqual(result, 2)
