from sys import stdin

answer = 0
worksheet = [line.rstrip("\n") for line in stdin if line.strip()]

pos = start_pos = len(worksheet[0]) - 1
while pos >= 0:
    if worksheet[-1][pos] == " ":
        pos -= 1
        continue

    operation = worksheet[-1][pos]
    numbers = [int("".join(worksheet[i][j] for i in range(len(worksheet)-1)))
               for j in range(pos, start_pos + 1)]

    if operation == "+":
        answer += sum(numbers)
    elif operation == "*":
        prod = 1
        for n in numbers:
            prod *= n
        answer += prod

    pos -= 1
    start_pos = pos - 1

print(answer)
