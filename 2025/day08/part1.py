from sys import stdin

boxes = []
for line in stdin:
    x, y, z = map(int, line.strip().split(','))
    boxes.append((x, y, z))
n = len(boxes)

distances = []
for i in range(n):
    x1, y1, z1 = boxes[i]
    for j in range(i + 1, n):
        x2, y2, z2 = boxes[j]
        dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        distances.append((dist_sq, i, j))
distances.sort(reverse=True)

parent = list(range(n))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(1000):
    _, i, j = distances.pop()
    root_i, root_j = find(i), find(j)
    if root_i != root_j:
        parent[root_i] = root_j

component_sizes = {}
for i in range(n):
    root = find(i)
    component_sizes[root] = component_sizes.get(root, 0) + 1

sizes = list(component_sizes.values())
sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])
