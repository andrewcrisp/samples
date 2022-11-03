import random
import pygame
from colors import *

class Cell:
    def __init__(self, x, y, width, height, xmax, ymax):
        self.visited = False
        self.cell_width = width
        self.cell_height = height
        self.index = (x + (y*xmax))
        self.x = x * self.cell_width
        self.y = y * self.cell_height
        
        self.top_wall =    ((self.x, self.y)                   , (self.x + self.cell_width, self.y))
        self.right_wall =  ((self.x + self.cell_width, self.y) , (self.x + self.cell_width, self.y + self.cell_height))
        self.bottom_wall = ((self.x, self.y + self.cell_height), (self.x + self.cell_width, self.y + self.cell_height))
        self.left_wall =   ((self.x, self.y)                   , (self.x, self.y + self.cell_height))
        self.rect = pygame.Rect((self.x, self.y), (self.cell_width, self.cell_height))
        self.walls = {'top' : True,
                     'right' : True,
                     'bottom' : True,
                     'left' : True}
        self.neighbors = {'top' : self.index - xmax,
                         'right' : self.index + 1,
                         'bottom' : self.index + xmax,
                         'left' : self.index - 1}
        
        if self.x == 0:
            del self.neighbors['left']
        if self.x == (xmax - 1) * width:
            del self.neighbors['right']
        if self.y == 0:
            del self.neighbors['top']
        if self.y == (ymax - 1) * height:
            del self.neighbors['bottom']
        for n in self.neighbors.keys():
            if self.neighbors[n] < 0 or self.neighbors[n] > (xmax * ymax):
                del self.neighbors[n]
        
    def Check_Neighbors(self, cells):
        available_neighbors = []
        chosen_neighbor = None
        for n in self.neighbors.keys():
            if not cells[self.neighbors[n]].visited:
                available_neighbors.append(self.neighbors[n])
        if len(available_neighbors) > 0:
            chosen_neighbor = random.randint(0, len(available_neighbors)-1)
            chosen_neighbor = available_neighbors[chosen_neighbor]
        return chosen_neighbor

    def Open_Wall(self, neighbor):
        if self.index == neighbor.index + 1:
            self.walls['left'] = False
        elif self.index == neighbor.index - 1:
            self.walls['right'] = False
        elif self.index > neighbor.index:
            self.walls['top'] = False
        elif self.index < neighbor.index:
            self.walls['bottom'] = False

    def Show(self, surface):
        if self.visited:
            surface.fill(mountbatten_pink, self.rect)
        if self.walls['top']:
            pygame.draw.line(surface, white, self.top_wall[0], self.top_wall[1])
        if self.walls['right']:
            pygame.draw.line(surface, white, self.right_wall[0], self.right_wall[1])
        if self.walls['bottom']:
            pygame.draw.line(surface, white, self.bottom_wall[0], self.bottom_wall[1])
        if self.walls['left']:
            pygame.draw.line(surface, white, self.left_wall[0], self.left_wall[1])

    def Highlight(self, surface):
        surface.fill(turquoise, self.rect)
