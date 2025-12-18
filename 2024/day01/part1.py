from sys import stdin

a, b = [], []
for line in stdin:
    if not line.strip():
        continue
    ai, bi = map(int, line.split())
    a.append(ai)
    b.append(bi)

a.sort()
b.sort()

answer = 0
for ai, bi in zip(a, b):
    answer += abs(ai - bi)

print(answer)
