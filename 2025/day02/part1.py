from sys import stdin

answer = 0
for i in stdin.read().split(','):
    start, end = map(int, i.strip().split('-'))

    for num in range(start, end + 1):
        number = str(num)
        length = len(number)

        if length % 2 != 0:
            continue
        if number[:length//2] == number[length//2:]:
            answer += num

print(answer)
