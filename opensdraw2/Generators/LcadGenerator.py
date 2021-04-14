class LcadGenerator:

    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return self._print_parts()

    def _print_parts(self):
        model_str = ""
        for part in self.model.parts:
            model_str += repr(part)

        return model_str
