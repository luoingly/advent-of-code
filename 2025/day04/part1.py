from sys import stdin
from itertools import product

grid = [line.strip() for line in stdin if line.strip()]
rows, cols = len(grid), len(grid[0])

answer = 0
for r, c in product(range(rows), range(cols)):
    if grid[r][c] != '@':
        continue

    count = 0
    for dr, dc in product([-1, 0, 1], repeat=2):
        if dr == 0 and dc == 0:
            continue

        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1

    if count < 4:
        answer += 1

print(answer)
