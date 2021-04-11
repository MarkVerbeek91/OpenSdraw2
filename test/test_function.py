import os
import unittest
import mock

from opensdraw2.opensdraw2 import OpenSdraw2
from opensdraw2.Function import Function, Arguments
from opensdraw2.Math import Add


class TestFunction(unittest.TestCase):
    def test_function_with_addition_no_arguments(self):
        add_mock = mock.Mock(Add)
        add_mock.return_value = 3
        func = Function(None, "name", [], add_mock)
        self.assertEqual(3, func())

    def test_function_with_addition_with_one_arguments(self):
        add_mock = mock.Mock(Add)
        add_mock.return_value = 3
        func = Function(None, "name", [], add_mock)
        self.assertEqual(3, func(2))


class TestArguments(unittest.TestCase):
    def test_function_with_addition_no_arguments(self):
        args = Arguments(None, None)


class TestOpenSdrawFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file_path = os.path.join('reference_models', 'single_part.lcad2')
        self.open_sdraw2 = OpenSdraw2()

    def test_single_add_function_zero_arguments(self):
        file_content = "( def function_name () ( + 1 2 ) )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            lcad_function = model.model_elements[0]

        self.assertEqual(3, lcad_function())

    def test_single_add_function_one_arguments(self):
        file_content = "( def function_name (arg1) ( + 1 args1 ) )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            lcad_function = model.model_elements[0]

        self.assertEqual(2, lcad_function(2))


if __name__ == '__main__':
    unittest.main()
