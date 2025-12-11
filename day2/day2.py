from common.file_reader import FileReader
import os

sampleFilename = os.path.join(os.path.dirname(__file__), 'sampleInput.txt')
inputFilename = os.path.join(os.path.dirname(__file__), 'input.txt')

def find_invalid_ids(start, end, divisor):
    ids = set()
    for i in range(find_first_sequence_number(start, divisor), find_last_sequence_number(end, divisor) + 1):
        ids.add(int(str(i)*divisor))
    return ids

def find_first_sequence_number(n, d):
    if len(n) % d == 0:
        seq = n[:len(n)//d]
        if int(seq*d) < int(n):
            return int(seq) + 1
        return int(seq)
    return 10**(len(n)//d)
    
def find_last_sequence_number(n, d):
    if len(n) % d == 0:
        seq = n[:len(n)//d]
        if int(seq*d) > int(n):
            return int(seq) - 1
        return int(seq)
    return 10**(len(n)//d) - 1

class Day2:
    def __init__(self, part):
        self.__part = part

    def get_answer(self, file_path):
        self.__file_path = file_path
        result = self.process_file_lines()
        self.print_result(result)

    def process_file_lines(self):
        file_reader = FileReader(self.__file_path)
        line = file_reader.read_lines()[0]
        ranges = [r.split('-') for r in line.split(',')]
        total = 0
        for r in ranges:
            start = r[0]
            end = r[1]
            if self.__part == 1:
                r = range(2, 3)
            else:
                r = range(2, len(end)+1)
            ids = set()
            for divisor in r:
                ids.update(find_invalid_ids(start, end, divisor))
            total += sum(ids)
        return total
            
    def print_result(self, result):
        print('Part {} answer for {}: {}'.format(self.__part, os.path.basename(self.__file_path), result))

def main():
    day1 = Day2(1)
    day1.get_answer(sampleFilename) # 1227775554
    day1.get_answer(inputFilename) # 30323879646
    day1 = Day2(2)
    day1.get_answer(sampleFilename) # 4174379265
    day1.get_answer(inputFilename) # 43872163557

if __name__ == "__main__":
    main()