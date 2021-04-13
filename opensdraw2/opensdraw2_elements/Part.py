class Part:
    def __init__(self, parent, name, position, orientation, color):
        self.parent = parent
        self.name = name
        self.position = position
        self.orientation = orientation
        self.color = color

    def __repr__(self):
        return "1 {color} {pos} {ori} {name}".format(color=self.color,
                                                     pos=self.get_position_str(),
                                                     ori=self.get_orientation_str(),
                                                     name=self.name)

    def get_position_str(self) -> str:
        return repr(self.position)

    def get_orientation_str(self) -> str:
        return repr(self.orientation)

