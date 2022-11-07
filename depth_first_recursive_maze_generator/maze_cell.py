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
        self.neighbors = {'top'   : (x + ((y - 1) * maze_width)),
                         'right'  : ((x + 1) + (y * maze_width)),
                         'bottom' : (x + ((y + 1) * maze_width)),
                         'left'   : ((x - 1) + (y * maze_width))
                         }
        if self.x == 0:
            del self.neighbors['left']
        if self.x == (maze_width - 1):
            del self.neighbors['right']
        if self.y == 0:
            del self.neighbors['top']
        if self.y == (maze_height - 1):
            del self.neighbors['bottom']

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
        tl = (x, y)
        tr = (x + cell_width, y)
        br = (x + cell_width, y + cell_height)
        bl = (x, y + cell_height)

        if self.visited:
            surface.fill(mountbatten_pink, pygame.Rect((x, y), (cell_width, cell_height)))
        if self.walls['top']:
            pygame.draw.line(surface, white, tl, tr)
        if self.walls['right']:
            pygame.draw.line(surface, white, tr, br)
        if self.walls['bottom']:
            pygame.draw.line(surface, white, br, bl)
        if self.walls['left']:
            pygame.draw.line(surface, white, tl, bl)

    def Highlight(self, surface, cell_width, cell_height):
        x = self.x * cell_width
        y = self.y * cell_height
        surface.fill(turquoise,
            pygame.Rect((x, y), (cell_width, cell_height)))
