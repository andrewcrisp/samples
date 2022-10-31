import sys
import pygame
import random
from colors import *
from cell import Cell


pygame.init()

size = height, width = (320, 240)
cell_width = 10
cell_height = 10
ncols = width / cell_width
nrows = height / cell_height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() 

cells = []

for j in range(ncols):
    for i in range(nrows):
        cell = Cell(i, j, cell_width, cell_height, ncols, nrows)
        cells.append(cell)

print("ncols: ", ncols)
#print("nrows: ", nrows)
#print("cells: ", nrows * ncols)
#print("cells: ", len(cells))
select_cell = random.randint(0, len(cells)-1)
select_cell = (nrows*ncols) - nrows
current = cells[select_cell]
print("starting:  ", current.index)
print(current.neighbors)
print(current.x, ", ", current.y)
cell_stack = []

while True:
#for i in range(30):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    for cell in cells:
        cell.Show(screen)
    
    current.visited = True
    #print("Current:   ", current.index, ", x: ", current.x, ", y: ", current.y)
    next_cell = current.Check_Neighbors(cells)
    #next_cell = current.index
    #print(current.neighbors)
    #print("next cell: ", next_cell)
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
    #print(current)
    pygame.display.update()
    #pygame.display.flip()
    clock.tick(60)
