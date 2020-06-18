import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 2), 7)

    def test_multiply(self):
        self.assertEqual(katas.multiply(6, 9), 54)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3)


if __name__ == '__main__':
    unittest.main()
