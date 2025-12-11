from sys import stdin

answer = 0
for i in stdin.read().split(','):
    start, end = map(int, i.strip().split('-'))

    for num in range(start, end + 1):
        number = str(num)
        length = len(number)

        for j in range(1, length//2+1):
            if number.replace(number[:j], '') == '':
                answer += num
                break

print(answer)