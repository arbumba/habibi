import unittest
from Lesson8 import*

class MyTest(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a = 10, b = 12), 22)

    def test_mixed(self):
        self.assertEqual(adder(1, a = 4), 5)

if __name__ == '__Lesson8__':
    unittest.main()