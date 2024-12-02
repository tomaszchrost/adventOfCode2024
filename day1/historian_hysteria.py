from advent_of_code.utils import data_reading
from advent_of_code.utils.data_reading.two_vertical_arrays import TwoVerticalArrays


def sort_data(data):
    new_data = [[],[]]
    new_data[0] = sorted(data[0])
    new_data[1] = sorted(data[1])
    return new_data

def get_sum_of_differences(data):
    sum_of_differences = 0
    for i in range(0, len(data[0])):
        sum_of_differences += abs(data[0][i] - data[1][i])
    return sum_of_differences

def count_occurrences_and_remove_less_than_values(a: int, b: [int]):
    count = 0
    for i in range(0, len(b)):
        if a == b[i]:
            count += 1
        elif a < b[i]:
            return count, b[i-count:]
    return count, []

def get_similarity_score(data):
    similarity_score = 0
    for i in range(0, len(data[0])):
        current_int = data[0][i]
        occurrences, data[1] = count_occurrences_and_remove_less_than_values(current_int, data[1])
        similarity_score += occurrences * current_int
    return similarity_score

def historian_hysteria_example_part1():
    data_reader = data_reading.TwoVerticalArrays()
    data: [[int][int]] = data_reader.get_data("example.txt")
    data = sort_data(data)
    sum_of_differences = get_sum_of_differences(data)
    print(sum_of_differences)

def historian_hysteria_part1():
    data_reader = data_reading.TwoVerticalArrays()
    data: [[int][int]] = data_reader.get_data("real.txt")
    data = sort_data(data)
    sum_of_differences = get_sum_of_differences(data)
    print(sum_of_differences)

def historian_hysteria_example_part2():
    data_reader = data_reading.TwoVerticalArrays()
    data: [[int][int]] = data_reader.get_data("example.txt")
    data = sort_data(data)
    print(get_similarity_score(data))

def historian_hysteria_part2():
    data_reader = data_reading.TwoVerticalArrays()
    data: [[int][int]] = data_reader.get_data("real.txt")
    data = sort_data(data)
    print(get_similarity_score(data))

if __name__=="__main__":
    print("Example Part 1")
    historian_hysteria_example_part1()
    print("Part 1")
    historian_hysteria_part1()
    print("Example Part 2")
    historian_hysteria_example_part2()
    print("Part 2")
    historian_hysteria_part2()