from sys import stdin

k = 2
answer = 0
for s in stdin:
    to_del = len(s.strip()) - k
    stack = []

    for ch in s.strip():
        while stack and stack[-1] < ch and to_del > 0:
            stack.pop()
            to_del -= 1
        stack.append(ch)

    answer += int(''.join(stack[:k]))

print(answer)
