import unittest

from opensdraw2.opensdraw2_elements.Math import Add


class TestAddClass(unittest.TestCase):

    def test_add_two_numbers(self):
        add = Add(None, 1, 2)
        self.assertEqual(3, add())

    def test_add_two_numbers_one_argument(self):
        add = Add(None, 1, 'arg')
        self.assertEqual(3, add(arg=2))

    def test_add_two_numbers_two_arguments(self):
        add = Add(None, 'foo', 'bar')
        self.assertEqual(3, add(foo=1, bar=2))


if __name__ == '__main__':
    unittest.main()
