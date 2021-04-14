class Add:
    def __init__(self, parent, num1, num2):
        self.parent = parent

        if not isinstance(num1, str):
            setattr(self, "number1", num1)

        if not isinstance(num2, str):
            setattr(self, "number2", num2)

    def __call__(self, **kwargs):
        num1 = self.number1 if hasattr(self, 'number1') else kwargs.popitem()[1]
        num2 = self.number2 if hasattr(self, 'number2') else kwargs.popitem()[1]

        return num1 + num2

