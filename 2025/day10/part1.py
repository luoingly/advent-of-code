from sys import stdin
from itertools import combinations

answer = 0
for line in stdin:
    diagram_part, *button_parts, _ = line.strip().split(' ')
    diagram = set(i for i in range(len(diagram_part)-2)
                  if diagram_part[i+1] == '#')
    buttons = [set(map(int, part.strip('()').split(',')))
               for part in button_parts]
    for i in range(1, len(buttons) + 1):
        for combo in combinations(buttons, i):
            combined = set()
            for button in combo:
                combined ^= button
            if combined == diagram:
                answer += i
                break
        else:
            continue
        break

print(answer)
