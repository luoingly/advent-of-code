from sys import stdin

position = 50
zero_count = 0

for line in stdin:
    instruction = line.strip()
    if not instruction:
        continue

    direction = instruction[0]
    distance = int(instruction[1:])

    if direction == 'L':
        for _ in range(distance):
            position = (position - 1) % 100
            if position == 0:
                zero_count += 1
    else:
        for _ in range(distance):
            position = (position + 1) % 100
            if position == 0:
                zero_count += 1

print(zero_count)
