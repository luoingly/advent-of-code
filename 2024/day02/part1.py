from sys import stdin

reports = [list(map(int, line.strip().split()))
           for line in stdin if line.strip()]

def is_safe(report: list[int]) -> bool:
    differences = [report[i] - report[i - 1] for i in range(1, len(report))]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False
    if not (all(diff >= 0 for diff in differences) or
            all(diff <= 0 for diff in differences)):
        return False
    return True

print(sum(1 for report in reports if is_safe(report)))
