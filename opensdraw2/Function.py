class Function:
    def __init__(self, parent, name, args, body):
        self.parent = parent
        self.name = name
        self.args = args
        self.body = body

    def __call__(self, *args):
        return self.body() if len(args) == 0 else self.body({self.args[0]: args})


class Arguments:
    def __init__(self, parent, args):
        self.parent = parent
        self.args = args

    def construct_argument(self, *args):
        return dict(zip(self.args, args))
