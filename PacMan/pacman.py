import pygame
from time import sleep
from random import randint
from colors import Colors
from cell import Cell
from grid import Grid
import time

class Game:
    def __init__(self, screen_width, screen_height, cell_width, cell_height, cell_rows, cell_cols):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode((screen_width, screen_height))
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rows = cell_rows
        self.cols = cell_cols

        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cells_by_coord = []
        self.cells_by_indices = []

        self.grid_obj = Grid(0, 0, [])
        self.cell_matrix = []

        self.pacman_actor = "img/pacman.png"
        self.pacman_rect = pygame.Rect(0, 0, 0, 0)
        self.pacman_index = (1, 5)
        self.ghost_index = (5, 0)
        self.ghost_rect = pygame.Rect(0, 0, 0, 0)

        self.margin = 10
        self.create_grid()
        self.main()

    def create_grid(self):
        for row in range(self.rows):
            raw_cell_matrix = []
            for col in range(self.cols):
                x = (self.cell_width * col) + (self.margin * (col + 1))
                y = (self.cell_height * row) + (self.margin * (row + 1))

                if (row, col) == self.pacman_index:
                    raw_cell_matrix.append(self.add_actor((x, y), (row, col), actor="pacman"))
                elif (row, col) == self.ghost_index:
                    raw_cell_matrix.append(self.add_actor((x, y), (row, col), actor="ghost"))
                else:
                    self.draw_cell(x, y, Colors.BLUE)

                    self.cells_by_coord.append(Cell(x, y))
                    self.cells_by_indices.append(Cell(row, col))
                    raw_cell_matrix.append(Cell(x, y))

            self.cell_matrix.append(raw_cell_matrix)

    def add_actor(self, coords: tuple, indices: tuple, actor: str):
        x, y = coords

        if actor == "pacman":
            self.pacman_rect = self.draw_actor(x, y, self.pacman_actor)
        elif actor == "ghost":
            self.ghost_rect = self.draw_cell(x, y, Colors.RED)

        self.cells_by_coord.append(Cell(x, y))
        self.cells_by_indices.append(Cell(indices[0], indices[1]))

        return Cell(x, y)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_frame(self, rect, color=Colors.WHITE):
        frame = pygame.draw.rect(self.DISPLAY, color, rect)
        pygame.display.update()
        return frame

    def draw_cell(self, x, y, color=Colors.WHITE):
        cell = pygame.draw.rect(self.DISPLAY, color, [x, y, self.cell_width, self.cell_height])
        return cell

    def draw_actor(self, x, y, actor_image):
        img = pygame.image.load(actor_image)
        img_rect = pygame.Surface.blit(self.DISPLAY, img, (x, y, 0, 0))
        return img_rect

    def move_actor(self, x_off, y_off):
        init_x, init_y = self.pacman_rect.x, self.pacman_rect.y
        img = pygame.image.load(self.pacman_actor)
        return pygame.Surface.blit(self.DISPLAY, img, (init_x + x_off, init_y + y_off, 0, 0))

    def move_to(self, x, y):
        img = pygame.image.load(self.pacman_actor)
        return pygame.Surface.blit(self.DISPLAY, img, (x, y, 0, 0))

    def convert_to_cell_type_path(self, path):
        cell_path = []
        for raw_cell in path:
            i, j = raw_cell.get_x(), raw_cell.get_y()
            cell = self.cell_matrix[i][j]
            cell_path.append(cell)
        return cell_path

    def main(self):
        print("WELCOME TO PACMAN!")
        game_exit = False

        frame = self.draw_frame(
            [self.screen_width + self.margin, self.screen_height + self.margin, 0.75 * self.screen_width,
             0.75 * self.screen_height])

        Game.update()
        self.grid_obj = Grid(self.rows, self.cols, self.cells_by_indices)
        shortest_path = self.grid_obj.get_shortest_path(Cell(self.pacman_index[0], self.pacman_index[1]),
                                                        Cell(self.ghost_index[0], self.ghost_index[1]))

        shortest_path = self.convert_to_cell_type_path(shortest_path)

        for p in shortest_path:
            print(p.x, p.y)
            self.move_to(p.x, p.y)
            time.sleep(1)
            Game.update()


        '''for p in shortest_path:
            p.display()
            print(end=' -> ' if shortest_path.index(p) != len(shortest_path) - 1 else " ")'''

        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pass


game = Game(600, 600, 75, 75, 7, 7)
sleep(1)
