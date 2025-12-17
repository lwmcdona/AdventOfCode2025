from common.file_reader import FileReader
import os
from enum import Enum
from collections import defaultdict

sampleFilename = os.path.join(os.path.dirname(__file__), 'sampleInput.txt')
inputFilename = os.path.join(os.path.dirname(__file__), 'input.txt')

class Vectors(Enum):
    N = (0, -1)
    NE = (1, -1)
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    SW = (-1, 1)
    W = (-1, 0)
    NW = (-1, -1)

PAPER = '@'

class Grid():
    def __init__(self, grid):
        self.__grid = grid.copy()
        self.__height = len(self.__grid)
        self.__width = len(self.__grid[0])
        self.__deltas = [vector.value for vector in Vectors]
        self.__neighbours = self.find_neighbours()

    def get_value(self, pos):
        return self.__grid[pos[0]][pos[1]]
    
    def set_value(self, pos, value):
        self.__grid[pos[0]][pos[1]] = value

    def get_accessible(self):
        return [pos for pos in self.__neighbours if len(self.__neighbours[pos]) < 4]

    def get_neighbours(self):
        return self.__neighbours
    
    def find_neighbours(self):
        self.__neighbours = defaultdict(set)
        for i in range(self.height()):
            for j in range(self.width()):
                pos = (i, j)
                if self.get_value(pos) == PAPER:
                    self.__neighbours[pos] = [n for n in self.find_neighbours_pos(pos) if self.get_value(n) == PAPER]
        return self.__neighbours

    def find_neighbours_pos(self, pos):
        (x, y) = pos
        return [(x + dx, y + dy) for (dx, dy) in self.__deltas if self.__is_valid_position((x + dx, y + dy))]

    def remove_pos(self, v):
        for neighbour in self.__neighbours[v]:
            self.__neighbours[neighbour].remove(v)
        del self.__neighbours[v]

    def width(self):
        return self.__width
    
    def height(self):
        return self.__height

    def __is_valid_position(self, pos):
        if pos[0] >= 0 and pos[0] < self.__height and pos[1] >= 0 and pos[1] < self.__width:
            return True
        return False

class Day4:
    PAPER = '@'
    def __init__(self, part):
        self.__part = part
        self.__grid = None

    def get_answer(self, file_path):
        self.__file_path = file_path
        result = self.process_file_lines()
        self.print_result(result)

    def process_file_lines(self):
        file_reader = FileReader(self.__file_path)
        lines = [[c for c in line.strip()] for line in file_reader.read_lines()]
        self.__grid = Grid(lines)
        accessible = self.__grid.get_accessible()
        total = len(accessible)
        if self.__part == 2:
            while len(accessible) > 0:
                for pos in accessible:
                    self.__grid.remove_pos(pos)
                accessible = self.__grid.get_accessible()
                total += len(accessible)
        return total
            
    def print_result(self, result):
        print('Part {} answer for {}: {}'.format(self.__part, os.path.basename(self.__file_path), result))

def main():
    day4 = Day4(1)
    day4.get_answer(sampleFilename) # 13
    day4.get_answer(inputFilename) # 1320
    day4 = Day4(2)
    day4.get_answer(sampleFilename) # 43
    day4.get_answer(inputFilename) # 8354

if __name__ == "__main__":
    main()