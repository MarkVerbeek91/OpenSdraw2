class Function:
    def __init__(self, parent, name, args, body):
        self.parent = parent
        self.name = name
        self.args = args
        self.body = body

    def __call__(self, *args):
        foo = self.args(*args)
        return self.body(**foo)


class Arguments:
    def __init__(self, parent, args):
        self.parent = parent
        self.args = args

    def __call__(self, *args):
        return {arg_name: arg_value for arg_name, arg_value in zip(self.args, args)}
