from sys import stdin

points = []
for line in stdin:
    if not line.strip():
        continue
    points.append(tuple(map(int, line.split(','))))
n = len(points)

unique_x = sorted(set(x for x, _ in points))
unique_y = sorted(set(y for _, y in points))
x_index = {x: i for i, x in enumerate(unique_x)}
y_index = {y: i for i, y in enumerate(unique_y)}

width, height = len(unique_x), len(unique_y)
grid = [[False] * height for _ in range(width)]

for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
    if x1 == x2:
        yi1, yi2 = sorted((y_index[y1], y_index[y2]))
        for yi in range(yi1, yi2 + 1):
            grid[x_index[x1]][yi] = True
    else:
        xi1, xi2 = sorted((x_index[x1], x_index[x2]))
        for xi in range(xi1, xi2 + 1):
            grid[xi][y_index[y1]] = True

edges = list(zip(points, points[1:] + points[:1]))
for yj, y in enumerate(unique_y):
    x_hits = []
    for (x1, y1), (x2, y2) in edges:
        if x1 != x2:
            continue
        ymin, ymax = sorted((y1, y2))
        if ymin <= y < ymax:
            x_hits.append(x1)
    if not x_hits:
        continue

    x_hits.sort()
    for i in range(0, len(x_hits), 2):
        x_left = x_hits[i]
        x_right = x_hits[i+1]
        xi_left = x_index[x_left]
        xi_right = x_index[x_right]
        for xi in range(xi_left + 1, xi_right):
            grid[xi][yj] = True

max_area = 0
for i in range(n):
    x1, y1 = points[i]
    for j in range(i+1, n):
        x2, y2 = points[j]
        in_loop = True
        for xi in range(min(x_index[x1], x_index[x2]), max(x_index[x1], x_index[x2]) + 1):
            for yj in range(min(y_index[y1], y_index[y2]), max(y_index[y1], y_index[y2]) + 1):
                if not grid[xi][yj]:
                    in_loop = False
                    break
            if not in_loop:
                break
        if in_loop:
            width, height = abs(x1 - x2) + 1, abs(y1 - y2) + 1
            max_area = max(max_area, width * height)

print(max_area)
