from cell import Cell
from graph import Graph


class Grid:
    def __init__(self, grid_rows, grid_cols, grid_cells):
        if len(grid_cells) != grid_rows * grid_cols:
            raise Warning("Invalid cell count or dimensions!")

        self.rows = grid_rows
        self.cols = grid_cols
        self.size = grid_rows * grid_cols
        self.cells = grid_cells
        self.grid = []

        index = 0
        for row in range(grid_rows):
            raw_grid = []
            for cols in range(grid_cols):
                raw_grid.append(grid_cells[index])
                index += 1

            self.grid.append(raw_grid)

    def get_cell_by_indices(self, i, j):
        return self.grid[i][j]

    def __repr__(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                print(cell)
            print()

    def get_adjacent_cells(self, cell):
        x, y = cell.get_x(), cell.get_y()
        adjacent_cells = []

        if x > 0:
            adjacent_cells.append(Cell(x - 1, y))
        if x < self.rows - 1:
            adjacent_cells.append(Cell(x + 1, y))
        if y > 0:
            adjacent_cells.append(Cell(x, y - 1))
        if y < self.cols - 1:
            adjacent_cells.append(Cell(x, y + 1))

        return adjacent_cells

    def get_cell_index(self, cell):
        for i in range(self.size):
            curr_cell = self.cells[i]
            if curr_cell.equals(cell):
                return i
        return - 1

    def get_path_to_dest(self, dest, prev_cell, path):
        if prev_cell[dest] == -1:
            return []
        path.append(dest)
        self.get_path_to_dest(prev_cell[dest], prev_cell, path)
        return path

    def get_shortest_path(self, pacman, ghost):
        graph = Graph(self.size)

        for cell in self.cells:
            if cell.type == "WALL":
                continue

            adjacent_cells = self.get_adjacent_cells(cell)
            for adj_cell in adjacent_cells:
                cell_idx = self.get_cell_index(cell)
                adj_cell_idx = self.get_cell_index(adj_cell)

                if self.cells[adj_cell_idx].type == "WALL":
                    continue

                graph.add_edge(cell_idx, adj_cell_idx)
                graph.add_edge(adj_cell_idx, cell_idx)

        pacman_index = self.get_cell_index(pacman)
        ghost_index = self.get_cell_index(ghost)
        path_to_all_cells = graph.get_shortest_path(pacman_index, ghost_index)
        path_to_dest = self.get_path_to_dest(
            ghost_index, path_to_all_cells, [])
        path_to_dest.append(pacman_index)

        path_in_cells_form = []
        for path in path_to_dest:
            path_in_cells_form.append(self.cells[path])
        path_in_cells_form.reverse()
        return path_in_cells_form
