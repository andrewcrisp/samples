import pygame
from colors import *

class Maze_Cell:
    def __init__(self, x, y, maze_width, maze_height):
        self.x = x
        self.y = y
        self.index = x + (y * maze_width)
        self.walls = {'top' : True,
                     'right' : True,
                     'bottom' : True,
                     'left' : True}
        self.visited = False
        self.neighbors = {'top' : self.index - maze_width,
                         'right' : self.index + 1,
                         'bottom' : self.index + maze_width,
                         'left' : self.index - 1}
        if self.x == 0:
            del self.neighbors['left']
        if self.x == (maze_width - 1):
            del self.neighbors['right']
        if self.y == 0:
            del self.neighbors['top']
        if self.y == (maze_height - 1):
            del self.neighbors['bottom']
        for n in self.neighbors.keys():
            if self.neighbors[n] < 0 or self.neighbors[n] > (maze_width * maze_height):
                del self.neighbors[n]

    def Open_Wall(self, neighbor):
        if self.index == neighbor.index + 1:
            self.walls['left'] = False
        elif self.index == neighbor.index - 1:
            self.walls['right'] = False
        elif self.index > neighbor.index:
            self.walls['top'] = False
        elif self.index < neighbor.index:
            self.walls['bottom'] = False

    def Show(self, surface, cell_width, cell_height):
        x = self.x * cell_width
        y = self.y * cell_height
        if self.visited:
            surface.fill(mountbatten_pink,
                pygame.Rect((x, y), (x + cell_width, y + cell_height)))
        if self.walls['top']:
            pygame.draw.line(surface, white, pygame.math.Vector2(x, y), pygame.math.Vector2(x + cell_width, y))
        if self.walls['right']:
            pygame.draw.line(surface, white, pygame.math.Vector2(x + cell_width, y), pygame.math.Vector2(x + cell_width, y + cell_height))
        if self.walls['bottom']:
            pygame.draw.line(surface, white, pygame.math.Vector2(x, y + cell_height), pygame.math.Vector2(x + cell_width, y + cell_height))
        if self.walls['left']:
            pygame.draw.line(surface, white, pygame.math.Vector2(x, y), pygame.math.Vector2(x, y + cell_height))

    def Highlight(self, surface, cell_width, cell_height):
        x = self.x * cell_width
        y = self.y * cell_height
        surface.fill(turquoise,
            pygame.Rect((x, y), (x + cell_width, y + cell_height)))
