import sys
import pygame
from colors import *
from maze import Maze

maze_width = 64
maze_height = 48
maze = Maze(maze_width, maze_height)
maze.Generate()

pygame.init()
cell_width = 10
cell_height = 10
size = (maze_width * cell_width, maze_height * cell_height) # = (64, 48)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while True:
#for i in range(6):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for cell in maze.cells:
        cell.Show(screen, cell_width, cell_height)
    pygame.display.flip()
    clock.tick(1)
    