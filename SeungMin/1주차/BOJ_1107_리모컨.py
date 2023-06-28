N = int(input())
M = int(input())
broken = []
answer = abs(100 - N)
if M != 0:
    broken = list(map(str, input().rstrip().split()))

for num in range(1000001):
    trigger = 0
    for i in str(num):
        if i in broken:
            trigger = 1
            break
    if trigger == 0:
        answer = min(answer, abs(num - N) + len(str(num)))

print(answer)
