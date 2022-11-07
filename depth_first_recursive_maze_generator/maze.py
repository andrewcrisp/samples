import random
from maze_cell import Maze_Cell

class Maze:
    def __init__(self, width, height, seed = None):
        # if seed is None, random.seed() uses a system randomness source
        random.seed(seed)
        self.width = width
        self.height = height
        self.cells = [None] * (width * height)
        for j in range(height):
            for i in range(width):
                cell = Maze_Cell(i, j, width, height)
                self.cells[cell.index] = cell
        select_cell = random.randint(0, len(self.cells) -1)
        self.current = self.cells[select_cell]
        self.cell_stack = []
    
    def Generate(self):
        self.Generate_Step()
        while(len(self.cell_stack) > 0):
            self.Generate_Step()

    def Generate_Step(self):
        self.current.visited = True
        next_cell = self.Check_Neighbors()
        if next_cell is not None:
            self.cell_stack.append(self.current)
            next_cell = self.cells[next_cell]
            self.current.Open_Wall(next_cell)
            next_cell.Open_Wall(self.current)
            self.current = next_cell
        else:
            if len(self.cell_stack) > 0:
                self.current = self.cell_stack.pop()

    def Check_Neighbors(self):
        available_neighbors = []
        chosen_neighbor = None
        for n in self.current.neighbors.keys():
            neighbor = self.cells[self.current.neighbors[n]]
            if not neighbor.visited:
                available_neighbors.append(neighbor.index)
        if len(available_neighbors) > 0:
            chosen_neighbor = random.randint(0, len(available_neighbors)-1)
            chosen_neighbor = available_neighbors[chosen_neighbor]
        return chosen_neighbor

    def Draw(self, screen, cell_width, cell_height):
        for cell in self.cells:
            cell.Show(screen, cell_width, cell_height)
        self.current.Highlight(screen, cell_width, cell_height)
