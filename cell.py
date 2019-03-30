
class Cell:

    def __init__(self, x, y, cell_type=None):
        self.x = x
        self.y = y
        self.cell_types = ["ACTOR", "EMPTY", "WALL"]
        self.type = "EMPTY" if cell_type is None else cell_type

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def equals(self, cell):
        return self.x == cell.x and self.y == cell.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
