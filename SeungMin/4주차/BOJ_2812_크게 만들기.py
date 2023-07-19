import sys

N, K = map(int, sys.stdin.readline().split())
numbers = sys.stdin.readline().rstrip()
stack = []

for num in numbers:
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))