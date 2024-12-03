from advent_of_code.utils import data_reading

import re

def get_numbers_to_mul(data) -> [(str, str)]:
    return re.findall(r"mul\(([0-9]+),([0-9]+)\)", data)

def get_muls_and_toggles(data) -> [(str, str, str)]:
    return re.findall(r"(do\(\)|don't\(\))|mul\(([0-9]+),([0-9]+)\)", data)

def get_total_of_muls_and_toggles(file):
    data_reader = data_reading.Rows()
    data = data_reader.get_data(file, str)
    total = 0
    ignore = False
    for line in data:
        regex_out: [(str, str, str)] = get_muls_and_toggles(line)
        for value in regex_out:
            if value[0] == "do()":
                ignore = False
            elif value[0] == "don't()":
                ignore = True
            else:
                if ignore:
                    continue
                else:
                    total += int(value[1])*int(value[2])
    print(total)


def get_total_of_mults(file):
    data_reader = data_reading.Rows()
    data = data_reader.get_data(file, str)
    total = 0
    for line in data:
        numbers_to_mul: [(str, str)] = get_numbers_to_mul(line)
        for pair in numbers_to_mul:
            total += int(pair[0])*int(pair[1])
    print(total)

def example_part1():
    get_total_of_mults("example.txt")

def part1():
    get_total_of_mults("real.txt")

def example_part2():
    get_total_of_muls_and_toggles("example2.txt")

def part2():
    get_total_of_muls_and_toggles("real.txt")

if __name__ == '__main__':
    part2()