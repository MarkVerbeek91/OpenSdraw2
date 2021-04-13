import os
import unittest
import mock

from opensdraw2.opensdraw2 import OpenSdraw2


class TestOpenSdrawFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file_path = os.path.join('reference_models', 'single_part.lcad2')
        self.open_sdraw2 = OpenSdraw2()

    def test_add_function(self):
        file_content = "( + 1 2 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            add_function = model.model_elements[0]

        self.assertEqual(3, add_function())

    def test_add_function_with_first_number_as_argument(self):
        file_content = "( + arg 2 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            add_function = model.model_elements[0]

        self.assertEqual(3, add_function(arg=1))

    def test_add_function_with_second_number_as_argument(self):
        file_content = "( + 1 arg )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            add_function = model.model_elements[0]

        self.assertEqual(3, add_function(arg=2))

    def test_add_function_both_numbers_as_argument(self):
        file_content = "( + arg1 arg2 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            add_function = model.model_elements[0]

        self.assertEqual(3, add_function(arg1=2, arg2=1))

    def test_add_function_with_seoncd_number_as_argument_with_random_name(self):
        file_content = "( + 1 random_name_that_is_not_used_much )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            add_function = model.model_elements[0]

        self.assertEqual(3, add_function(arg=2))
