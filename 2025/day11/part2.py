from sys import stdin
from collections import deque

graph = {}
for line in stdin:
    name, outputs = line.strip().split(': ')
    graph[name] = outputs.split(' ')

all_nodes = set(graph.keys())
for node in graph.values():
    all_nodes.update(node)

reverse_graph = {node: [] for node in all_nodes}
for u in graph:
    for v in graph[u]:
        reverse_graph[v].append(u)

in_degree = {node: 0 for node in all_nodes}
for u in graph:
    for v in graph[u]:
        in_degree[v] += 1

queue = deque([node for node in all_nodes if in_degree[node] == 0])
topo_order = []
while queue:
    u = queue.popleft()
    topo_order.append(u)
    if u in graph:
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

node_to_idx = {node: i for i, node in enumerate(topo_order)}
idx_to_node = {i: node for i, node in enumerate(topo_order)}

n = len(topo_order)
dp = [[0] * 4 for _ in range(n)]
dp[node_to_idx['svr']][0] = 1
for u_idx in range(n):
    u = idx_to_node[u_idx]
    if u not in graph:
        continue

    for mask in range(4):
        if dp[u_idx][mask] == 0:
            continue

        for v in graph[u]:
            v_idx = node_to_idx[v]

            new_mask = mask
            if v == 'dac':
                new_mask = mask | 0b01
            elif v == 'fft':
                new_mask = mask | 0b10

            dp[v_idx][new_mask] += dp[u_idx][mask]

print(dp[node_to_idx['out']][0b11])
