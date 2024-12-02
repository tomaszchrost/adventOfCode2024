from copy import copy

from advent_of_code.utils import data_reading
from math import copysign

class ReportCheck:
    def __init__(self, data, min_diff, max_diff, allow_bad_level):
        self.data: [[int]] = data
        self.min_diff: int = min_diff
        self.max_diff: int = max_diff
        self.allow_bad_level: bool = allow_bad_level


    def total_safe_reports(self):
        total = 0
        for report in self.data:
            if self.allow_bad_level:
                total += int(self.is_report_safe_allow_bad_value(report))
            else:
                total += int(self.is_report_safe(report))
        return total

    def are_values_ok(self, a, b, correlation):
        diff = a - b
        abs_diff = abs(diff)
        return self.min_diff <= abs_diff <= self.max_diff and (correlation == copysign(1, diff) or correlation is None)

    def is_report_safe(self, report: [int]) -> bool:
        report_correlation = None
        for i in range(1, len(report)):
            if not self.are_values_ok(report[i], report[i - 1], report_correlation):
                return False
            report_correlation = copysign(1, report[i] - report[i - 1])
        return True

    def is_report_safe_allow_bad_value(self, report: [int]):
        if self.is_report_safe(report):
            print(report, True)
            return True

        for i in range(0, len(report)):
            new_report = copy(report)
            new_report.pop(i)
            if self.is_report_safe(new_report):
                print(report, True)
                return True
        print(report, False)
        return False

def run_part1(file):
    data_reader = data_reading.TwoDimensionalArray()
    data: [[int][int]] = data_reader.get_data(file, int)

    report_check = ReportCheck(data, 1, 3, False)
    return report_check.total_safe_reports()

def run_part2(file):
    data_reader = data_reading.TwoDimensionalArray()
    data: [[int][int]] = data_reader.get_data(file, int)
    report_check = ReportCheck(data, 1, 3, True)
    return report_check.total_safe_reports()

def example_part1():
    print("Part 1 Example: ",run_part1("example.txt"))

def part1():
    print("Part 1: ", run_part1("real.txt"))

def example_part2():
    print("Part 2 Example: ", run_part2("example.txt"))

def part2():
    print("Part 2: ", run_part2("real.txt"))

if __name__=="__main__":
    part2()