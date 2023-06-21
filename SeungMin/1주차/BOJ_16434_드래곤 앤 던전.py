import sys
import math

N, atk = map(int, input().split())
answer = 0
hp = 0
for i in range(N):
    t, a, h = map(int, sys.stdin.readline().rstrip().split())
    if t == 1:
        time = math.ceil(h/atk) - 1
        hp = hp - (time * a)
        answer = max(abs(hp) + 1, answer)
    else:
        atk = atk + a
        hp = min(0, hp + h)

print(answer)
