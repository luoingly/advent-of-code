from sys import stdin

diagram = [list(line.strip()) for line in stdin.readlines()]
height, width = len(diagram), len(diagram[0])

answer = 0
active = [False] * width
for y in range(height):
    new_active = [False] * width
    for x in range(width):

        if diagram[y][x] == 'S':
            new_active[x] = True

        elif diagram[y][x] == '^':
            if not active[x]:
                continue
            answer += 1
            if x > 0:
                new_active[x - 1] = True
            if x < width - 1:
                new_active[x + 1] = True

        else:
            if active[x]:
                new_active[x] = True
    active = new_active

print(answer)
