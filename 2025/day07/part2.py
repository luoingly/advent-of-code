from sys import stdin

diagram = [list(line.strip()) for line in stdin.readlines()]
height, width = len(diagram), len(diagram[0])

routes = [0] * width
for y in range(height):
    new_routes = [0] * width
    for x in range(width):

        if diagram[y][x] == 'S':
            new_routes[x] += 1

        elif diagram[y][x] == '^':
            if x > 0:
                new_routes[x - 1] += routes[x]
            if x < width - 1:
                new_routes[x + 1] += routes[x]

        else:
            new_routes[x] += routes[x]
    routes = new_routes

print(sum(routes))
