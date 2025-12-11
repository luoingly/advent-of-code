from sys import stdin

graph = {}
for line in stdin:
    name, outputs = line.strip().split(': ')
    graph[name] = outputs.split(' ')

def dfs(current: str) -> int:
    if current == 'out':
        return 1
    count = 0
    for output in graph.get(current, []):
        count += dfs(output)
    return count

print(dfs('you'))
