from sys import stdin

answer = 0
ranges = []
reading_ranges = True
for line in stdin:
    if line.strip() == "":
        reading_ranges = False
        continue

    if reading_ranges:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
        continue

    number = int(line.strip())
    for start, end in ranges:
        if start <= number <= end:
            answer += 1
            break

print(answer)
