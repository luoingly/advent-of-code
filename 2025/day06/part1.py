from sys import stdin

answer = 0
worksheet = [line.rstrip('\n') + ' ' for line in stdin if line.strip()]

pos = start_pos = 0
while pos < len(worksheet[0]):
    if not all(row[pos] == ' ' for row in worksheet):
        pos += 1
        continue

    operation = worksheet[-1][start_pos]
    numbers = [int(row[start_pos:pos].strip()) for row in worksheet[:-1]]

    if operation == '+':
        answer += sum(numbers)
    elif operation == '*':
        prod = 1
        for n in numbers:
            prod *= n
        answer += prod

    pos += 1
    start_pos = pos

print(answer)
