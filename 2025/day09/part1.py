from sys import stdin

points = []
for line in stdin:
    if not line.strip():
        continue
    points.append(tuple(map(int, line.split(','))))
n = len(points)

max_area = 0
for i in range(n):
    x1, y1 = points[i]
    for j in range(i+1, n):
        x2, y2 = points[j]
        width, height = abs(x1 - x2) + 1, abs(y1 - y2) + 1
        max_area = max(max_area, width * height)

print(max_area)
