import pygame
from colors import *

class Cell:
    x, y = 0, 0
    cell_width = 10
    cell_height = 10






    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top_wall = ((x, y), (x + self.cell_width, y))
        self.right_wall = ((x + self.cell_width, y), (x + self.cell_width, y + self.cell_height))
        self.bottom_wall = ((x, y + self.cell_height), (x + self.cell_width, y + self.cell_height))
        self.left_wall = ((x, y), (x, y + self.cell_height))

    def Show(self, surface):
        pygame.draw.line(surface, white, self.top_wall[0], self.top_wall[1])
        pygame.draw.line(surface, white, self.right_wall[0], self.right_wall[1])
        pygame.draw.line(surface, white, self.bottom_wall[0], self.bottom_wall[1])
        pygame.draw.line(surface, white, self.left_wall[0], self.left_wall[1])

