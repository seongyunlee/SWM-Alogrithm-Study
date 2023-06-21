import sys

sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == M-1 and y == N-1:
        return 1

    dp[x][y] = 0

    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]
        if 0 <= nextX <= M-1 and 0 <= nextY <= N-1:
            if nums[x][y] > nums[nextX][nextY]:
                dp[x][y] += dfs(nextX, nextY)
    return dp[x][y]

M, N = map(int, sys.stdin.readline().split())
nums = []
for i in range(M):
    nums.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1]*N for _ in range(M)]
print(dfs(0, 0))
