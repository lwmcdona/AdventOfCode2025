from common.file_reader import FileReader
import os

sampleFilename = os.path.join(os.path.dirname(__file__), 'sampleInput.txt')
inputFilename = os.path.join(os.path.dirname(__file__), 'input.txt')

class JoltageFinder():
    def __init__(self, batteries):
        self.__batteries = batteries

    def find_largest_digit(self, start, end):
        return sorted(self.__batteries[start:end])[-1]

    def find_max_voltage(self, n):
        index = 0
        digits = ''
        for i in range(n-1, -1, -1):
            d = self.find_largest_digit(index, len(self.__batteries)-i)
            index = self.__batteries.find(d, index) + 1
            digits += d
        return int(digits)

class Day3:
    def __init__(self, part):
        self.__part = part
        if part == 1:
            self.__digits = 2
        else: 
            self.__digits = 12

    def get_answer(self, file_path):
        self.__file_path = file_path
        result = self.process_file_lines()
        self.print_result(result)

    def process_file_lines(self):
        file_reader = FileReader(self.__file_path)
        lines = file_reader.read_lines()
        total = 0
        for line in lines:
            joltage_finder = JoltageFinder(line)
            total += joltage_finder.find_max_voltage(self.__digits)
        return total
            
    def print_result(self, result):
        print('Part {} answer for {}: {}'.format(self.__part, os.path.basename(self.__file_path), result))

def main():
    day3 = Day3(1)
    day3.get_answer(sampleFilename) # 357
    day3.get_answer(inputFilename) # 17155
    day3 = Day3(2)
    day3.get_answer(sampleFilename) # 3121910778619
    day3.get_answer(inputFilename) # 169685670469164

if __name__ == "__main__":
    main()