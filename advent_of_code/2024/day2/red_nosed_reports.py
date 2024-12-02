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
            total += int(self.is_report_safe(report))
        return total

    def are_values_ok(self, a, b, correlation):
        diff = a - b
        abs_diff = abs(diff)
        if self.min_diff > abs_diff > self.max_diff:
            return False



    def is_report_safe(self, report: [int]) -> bool:
        report_correlation = None
        bad_level_used = False
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            abs_diff = abs(diff)
            if abs_diff < self.min_diff or abs_diff > self.max_diff:
                if self.allow_bad_level and not bad_level_used:
                    bad_level_used = True

                    report.remove(i)
                else:
                    return False

            if report_correlation is None:
                report_correlation = copysign(1, diff)
            elif report_correlation != copysign(1, diff):
                if self.allow_bad_level and not bad_level_used:
                    bad_level_used = True
                    i = i - 1
                    report.remove(i)
                else:
                    return False
        return True

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

if __name__=="__main__":
    part1()