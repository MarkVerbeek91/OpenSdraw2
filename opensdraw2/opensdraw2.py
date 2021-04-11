import os

from textx import metamodel_from_file

from opensdraw2.Part import Part


class OpenSdraw2:

    def __init__(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.language = metamodel_from_file(os.path.join(dir_path, 'opensdraw.tx'))

    def load_model(self, model_file):
        model = self.language.model_from_file(model_file)

        for model_element in model.model_elements:
            print(model_element)


if __name__ == '__main__':
    pass
