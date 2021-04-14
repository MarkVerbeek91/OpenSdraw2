import os
import unittest
import mock

from opensdraw2.opensdraw2 import OpenSdraw2


class TestPart(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file_path = os.path.join('reference_models', 'single_part.lcad2')
        self.open_sdraw2 = OpenSdraw2()

    def test_creation_of_a_part(self):
        file_content = "( tb 1 2 3 0 0 0 'some_part' 4 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            part = model.model_elements[0]

        self.assertEqual("1 4 1 2 3 1 0 0 0 1 0 0 0 1 some_part\n", repr(part))

    def test_creation_of_a_part_on_a_90_degree_angle(self):
        file_content = "( tb 1 2 3 0 0 90 'some_part' 4 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            part = model.model_elements[0]

        self.assertEqual("1 4 1 2 3 0 -1 0 1 0 0 0 0 1 some_part\n", repr(part))

    def test_creation_of_a_part_on_a_45_degree_angle(self):
        file_content = "( tb 1 2 3 0 45 0 'some_part' 4 )"

        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            model = self.open_sdraw2.load_model(self.test_file_path)
            part = model.model_elements[0]

        num = 0.707106781  # sqrt(2)/2

        self.assertEqual("1 4 1 2 3 {n} 0 {n} 0 1 0 -{n} 0 {n} some_part\n".format(n=num), repr(part))


if __name__ == '__main__':
    unittest.main()
