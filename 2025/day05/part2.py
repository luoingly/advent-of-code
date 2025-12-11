from sys import stdin

ranges = []
for line in stdin:
    if line.strip() == "":
        break
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

ranges.sort(key=lambda x: x[0])
merged = [ranges[0]]

for current in ranges[1:]:
    last_merged = merged[-1]
    if current[0] <= last_merged[1] + 1:
        merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
    else:
        merged.append(current)

answer = 0
for start, end in merged:
    answer += end - start + 1

print(answer)
