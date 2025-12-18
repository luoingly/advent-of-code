from sys import stdin
from collections import Counter

a, b = [], []
for line in stdin:
    if not line.strip():
        continue
    ai, bi = map(int, line.split())
    a.append(ai)
    b.append(bi)

b_cnt = Counter(b)

answer = 0
for ai in a:
    answer += ai * b_cnt[ai]

print(answer)
