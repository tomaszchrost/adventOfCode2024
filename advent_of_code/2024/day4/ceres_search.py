from copy import copy

from advent_of_code.utils import data_reading
from advent_of_code.utils.direction import DIRECTION_LIST, move_valid, get_value_in_direction, UP_LEFT, \
    get_opposite_direction, DOWN_RIGHT, DOWN_LEFT, UP_RIGHT


class CeresSearch:
    def __init__(self):
        self.data = None
        self.word = "XMAS"

    def was_word_found(self, x, y, remainder_of_word, direction):
        if len(remainder_of_word) == 0:
            return True
        elif not move_valid(x, y, direction, self.data):
            return False

        new_x = x + direction.x_move
        new_y = y + direction.y_move
        if self.data[new_y][new_x] == remainder_of_word[0]:
            return self.was_word_found(new_x, new_y, remainder_of_word[1:], direction)
        else:
            return False

    def find_word_occurrences(self):
        word_occurrences = 0
        word_starts = "X"
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == word_starts:
                    for direction in DIRECTION_LIST:
                        word_occurrences += int(self.was_word_found(x, y, self.word[1:], direction))
        return word_occurrences

    def find_x_mas_occurrences(self):
        word_occurrences = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "A":
                    letters_to_find = ('M','S')
                    tuple1 = (get_value_in_direction(x, y, UP_LEFT, self.data), get_value_in_direction(x, y, DOWN_RIGHT, self.data))
                    tuple2 = (get_value_in_direction(x, y, UP_RIGHT, self.data), get_value_in_direction(x, y, DOWN_LEFT, self.data))

                    if (letters_to_find[0] in tuple1 and letters_to_find[1] in tuple1
                        and letters_to_find[0] in tuple2 and letters_to_find[1] in tuple2):
                        word_occurrences += 1
        return word_occurrences


def run_part1(file):
    data_reader = data_reading.TwoDimensionalArray()
    data: [[str]] = data_reader.get_data(file, str, False)
    ceres_search = CeresSearch()
    ceres_search.data = data
    return ceres_search.find_word_occurrences()

def run_part2(file):
    data_reader = data_reading.TwoDimensionalArray()
    data: [[str]] = data_reader.get_data(file, str, False)
    ceres_search = CeresSearch()
    ceres_search.data = data
    return ceres_search.find_x_mas_occurrences()

def example_part1():
    print("Part 1 Example: ", run_part1("example.txt"))

def part1():
    print("Part 1: ", run_part1("real.txt"))

def example_part2():
    print("Part 2 Example: ", run_part2("example.txt"))

def part2():
    print("Part 2: ", run_part2("real.txt"))

if __name__=="__main__":
    part2()