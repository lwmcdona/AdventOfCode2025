from common.file_reader import FileReader
import os

sampleFilename = os.path.join(os.path.dirname(__file__), 'sampleInput.txt')
inputFilename = os.path.join(os.path.dirname(__file__), 'input.txt')

class Dial:
    def __init__(self, part):
        self.__part = part
        self.__value = 50
        self.__zeroes = 0

    def get_password(self):
        return self.__zeroes

    def move(self, rotation):
        start = self.__value
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == 'L':
            distance = -distance
        self.__value += distance

        if self.__part == 2:
            if direction == 'R':
                self.__zeroes += self.__value // 100
            else:
                if start == 0:
                    self.__zeroes -= 1
                self.__zeroes += abs((self.__value - 1) // 100)
        
        self.__value %= 100

        if self.__part == 1 and self.__value == 0:
            self.__zeroes += 1

class Day1:
    def __init__(self, part):
        self.__part = part

    def get_answer(self, file_path):
        self.__file_path = file_path
        result = self.process_file_lines()
        self.print_result(result)

    def process_file_lines(self):
        file_reader = FileReader(self.__file_path)
        lines = file_reader.read_lines()

        dial = Dial(self.__part)
        for rotation in lines:
            dial.move(rotation)
        return dial.get_password()
    
    def print_result(self, result):
        print('Part {} answer for {}: {}'.format(self.__part, os.path.basename(self.__file_path), result))


def main():
    day1 = Day1(1)
    day1.get_answer(sampleFilename) # 3
    day1.get_answer(inputFilename) # 1168
    day1 = Day1(2)
    day1.get_answer(sampleFilename) # 6
    day1.get_answer(inputFilename) # 7199

if __name__ == "__main__":
    main()