import os
import unittest

from opensdraw2.opensdraw2 import OpenSdraw2


class MyTestCase(unittest.TestCase):

    def test_something(self):
        test_file = os.path.join('reference_models', 'single_part.lcad2')
        opensdraw2 = OpenSdraw2()

        opensdraw2.load_model(test_file)


if __name__ == '__main__':
    unittest.main()
