from cell import Cell
from grid import Grid


class Colors:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


'''cells = []
for r in range(7):
    for c in range(7):
        cells.append(Cell(r, c))

grid = Grid(7, 7, cells)
path = grid.get_shortest_path(Cell(1, 5), Cell(5, 0))
for p in path:
    p.display()
    print(end=" -> " if path.index(p) != len(path) - 1 else " ")'''
