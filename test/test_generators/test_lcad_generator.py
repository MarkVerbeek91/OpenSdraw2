import os
import unittest
import mock

from opensdraw2.Generators.LcadGenerator import LcadGenerator
from opensdraw2.LegoModel import LegoModel


def get_path(file_name):
    module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(module_path, 'reference_models', file_name)


class TestLcadGenerator(unittest.TestCase):

    @unittest.skip("not complete")
    def test_print_of_lego_model(self):
        lego_model = LegoModel(get_path('single_part.lcad2'))

        model_mock = mock.Mock()
        model_mock.get_parts.return_value = [""]

        lego_model.model = model_mock

        with open(get_path('single_part.lcad2')) as reference_model:
            self.assertEqual(reference_model.read(), repr(LcadGenerator(lego_model)))


if __name__ == '__main__':
    unittest.main()
