from logging import warn, warning
import random
import pygame
from colors import *

class Cell:
    def __init__(self, x, y, width, height, ncols, nrows):
        self.visited = False
        self.cell_width = width
        self.cell_height = height
        self.index = (x + (y*nrows))
        self.x = x * self.cell_width
        self.y = y * self.cell_height
        
        self.top_wall = ((self.x, self.y), (self.x + self.cell_width, self.y))
        self.right_wall = ((self.x + self.cell_width, self.y), (self.x + self.cell_width, self.y + self.cell_height))
        self.bottom_wall = ((self.x, self.y + self.cell_height), (self.x + self.cell_width, self.y + self.cell_height))
        self.left_wall = ((self.x, self.y), (self.x, self.y + self.cell_height))

        #self.index = (x/self.cell_width) + ((y/self.cell_height) * (ncols))
        self.walls = {'top' : True,
                     'right' : True,
                     'bottom' : True,
                     'left' : True}
        self.neighbors = {'top' : self.index - nrows,
                         'right' : self.index + 1,
                         'bottom' : self.index + nrows,
                         'left' : self.index - 1}
        
        if self.x == 0:
            del self.neighbors['left']
        if self.x == ncols:
            del self.neighbors['right']
        if self.y == 0:
            del self.neighbors['top']
        if self.y == nrows:
            del self.neighbors['bottom']
        for n in self.neighbors.keys():
            if self.neighbors[n] < 0 or self.neighbors[n] > (nrows * ncols):
                del self.neighbors[n]
        

    def Check_Neighbors(self, cells):
        #print(self.neighbors)
        available_neighbors = []
        chosen_neighbor = None
        for n in self.neighbors.keys():
            #print(n)
            #print(self.neighbors[n])
            if not cells[self.neighbors[n]].visited:
                available_neighbors.append(self.neighbors[n])
        if len(available_neighbors) > 0:
            chosen_neighbor = random.randint(0, len(available_neighbors)-1)
            chosen_neighbor = available_neighbors[chosen_neighbor]
        #print("chosen: ", chosen_neighbor)
        #print("Length of avail neighbors: ", len(available_neighbors))
        #print(available_neighbors)
        return chosen_neighbor

    def Open_Wall(self, neighbor):
        #print("my index:       ", self.index)
        #print("neighbor index: ", neighbor.index)
        removed = None
        if self.index == neighbor.index + 1:
            self.walls['left'] = False
            removed = "left"
        elif self.index == neighbor.index - 1:
            self.walls['right'] = False
            removed = "right"
        elif self.index > neighbor.index:
            self.walls['top'] = False
            removed = "top"
        elif self.index < neighbor.index:
            self.walls['bottom'] = False
            removed = "bottom"
        #print(removed)

    def Show(self, surface):
        if self.walls['top']:
            pygame.draw.line(surface, white, self.top_wall[0], self.top_wall[1])
        if self.walls['right']:
            pygame.draw.line(surface, white, self.right_wall[0], self.right_wall[1])
        if self.walls['bottom']:
            pygame.draw.line(surface, white, self.bottom_wall[0], self.bottom_wall[1])
        if self.walls['left']:
            pygame.draw.line(surface, white, self.left_wall[0], self.left_wall[1])
        #print(self.index)

    def Highlight(self, surface):
        r = pygame.Rect((self.x, self.y), (self.cell_width, self.cell_height))
        surface.fill(highlight, r)
        #print(self.walls)
        #print('highlighting')
        #pygame.draw.rect(surface, highlight, r, 0)