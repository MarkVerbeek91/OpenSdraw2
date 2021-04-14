from opensdraw2.opensdraw2 import OpenSdraw2


class LegoModel:
    def __init__(self, file_name):
        self.model = OpenSdraw2().load_model(file_name)

    @property
    def parts(self):
        for part in self.model.get_parts():
            yield part
