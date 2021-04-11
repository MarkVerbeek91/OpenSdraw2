import os

from textx import metamodel_from_file

from opensdraw2.Part import Part
from opensdraw2.Function import Function

opensdraw_classes = [Part, Function]


class OpenSdraw2:

    def __init__(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.language = metamodel_from_file(os.path.join(dir_path, 'opensdraw.tx'), classes=opensdraw_classes)

    def load_model(self, model_file):
        with open(model_file, 'r') as file_id:
            model_str = file_id.read()
        model = self.language.model_from_str(model_str)

        if isinstance(model, str):
            raise EmptyModelError

        for model_element in model.model_elements:
            if isinstance(model_element, Part):
                print(model_element.name)

        return model


class EmptyModelError(Exception):
    pass


if __name__ == '__main__':
    pass
