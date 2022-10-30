from re import S
import sys
import pygame
from colors import *
from cell import Cell

pygame.init()

size = width, height = 320, 240
cell_width = 10
cell_height = 10

screen = pygame.display.set_mode(size)

cells = []

for i in range(width / cell_width):
    for j in range(height / cell_height):
        cell = Cell(i*cell_width, j*cell_height)
        cells.append(cell)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    for cell in cells:
        cell.Show(screen)
    pygame.display.flip()
