import sys
input =sys.stdin.readline
N,M = map(int,input().split())
price = [int(input()) for _ in range(N)]
subSum = [0]
for p in range(N):
    subSum.append(subSum[-1]+price[p])
leftMin = subSum[0]
answer = sum(price[:M])
print(subSum)
for i in range(M,len(subSum)):
    print(i,leftMin)
    answer= max(answer,subSum[i]-leftMin)
    leftMin = min(leftMin,subSum[i-M+1])
print(answer)