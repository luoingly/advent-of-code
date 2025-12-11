from sys import stdin
from scipy.optimize import linprog

answer = 0
for line in stdin:
    _, *button_parts, joltage_part = line.strip().split(' ')
    joltage = list(map(int, joltage_part.strip('{}').split(',')))
    buttons = [set(map(int, part.strip('()').split(',')))
               for part in button_parts]
    counters_n = len(joltage)
    buttons_n = len(buttons)

    c = [1] * buttons_n
    A_eq = [[1 if j in buttons[i] else 0 for i in range(buttons_n)]
            for j in range(counters_n)]
    res = linprog(c, A_eq=A_eq, b_eq=joltage, integrality=1)
    answer += int(res.fun)

print(answer)
