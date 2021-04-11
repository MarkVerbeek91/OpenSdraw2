from scipy.spatial.transform import Rotation


class PositionVector:
    def __init__(self, parent, x, y, z):
        self.parent = parent
        self.position = [x, y, z]

    def __repr__(self):
        return " ".join([str(elm) for elm in self.position])


class RotationVector:
    def __init__(self, parent, r_x, r_y, r_z):
        self.parent = parent
        self.orientation = [r_x, r_y, r_z]

    def __repr__(self):
        r = Rotation.from_euler("xyz", self.orientation, degrees=True).as_matrix()
        return " ".join([self.num2str(num) for num in r.flatten().tolist()])

    @staticmethod
    def num2str(num):
        return f"{num:.9f}".rstrip('0').rstrip('.') if abs(num) > 1e-9 else "0"
