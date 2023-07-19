def solution(m, n, puddles):
    maps = [[0 for i in range(m + 1)] for j in range(n + 1)]
    maps[1][1] = 1
    answer = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            maps[i][j] = maps[i - 1][j] + maps[i][j - 1]
            if [j, i] in puddles:
                maps[i][j] = 0
    
    return maps[n][m] % 1000000007
