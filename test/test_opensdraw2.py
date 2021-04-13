import os
import unittest
import mock

from opensdraw2.opensdraw2 import OpenSdraw2
from opensdraw2.opensdraw2 import EmptyModelError


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file_path = os.path.join('reference_models', 'single_part.lcad2')
        self.open_sdraw2 = OpenSdraw2()

    def test_open_model(self):
        with mock.patch('builtins.open', mock.mock_open(read_data="")) as mock_open:
            with self.assertRaises(EmptyModelError):
                self.open_sdraw2.load_model(self.test_file_path)
            mock_open.assert_called_with(self.test_file_path, 'r')

    def test_single_import(self):
        file_content = "( import other_model )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)

        self.assertEqual(1, len(model.model_elements))

    def test_single_empty_function(self):
        file_content = "( def function_name () ( block ) )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)

        self.assertEqual(1, len(model.model_elements))

    def test_single_empty_block(self):
        file_content = "( block )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)

        self.assertEqual(1, len(model.model_elements))

    def test_single_technic_block(self):
        file_content = "( tb 1 2 3 0 0 0 'some_part' 4 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)

        self.assertEqual(1, len(model.model_elements))

    def test_single_block_with_one_part(self):
        file_content = "( block ( tb 1 2 3 0 0 0 'some_part' 4 ) )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)

        self.assertEqual(1, len(model.model_elements))

    def test_function_with_block_with_one_part(self):
        file_content = "( def func () ( block ( tb 1 2 3 0 0 0 'some_part' 4 ) ) )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)

        self.assertEqual(1, len(model.model_elements))


if __name__ == '__main__':
    unittest.main()
