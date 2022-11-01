import sys
import pygame
import random
from colors import *
from cell import Cell

pygame.init()

size = width, height = (640, 480)
cell_width = 10
cell_height = 10
xmax = width / cell_width
ymax = height / cell_height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cells = []

for j in range(ymax):
    for i in range(xmax):
        cell = Cell(i, j, cell_width, cell_height, xmax, ymax)
        cells.append(cell)

select_cell = random.randint(0, len(cells)-1)
current = cells[select_cell]

cell_stack = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    for cell in cells:
        cell.Show(screen)
    
    current.visited = True
    next_cell = current.Check_Neighbors(cells)
    if next_cell is not None:
        next_cell = cells[next_cell]
        current.Open_Wall(next_cell)
        next_cell.Open_Wall(current)
        cell_stack.append(current)
        current = next_cell
    else:
        if len(cell_stack) > 0:
            current = cell_stack.pop()
    
    current.Highlight(screen)
    pygame.display.update()
    clock.tick(180)
