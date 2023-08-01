N, M = map(int, input().split())
r, c, d = map(int, input().split())
R = [list(map(int, input().split())) for _ in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 0
while True:
    if R[r][c] == 0:
        ans += 1
        R[r][c] = 2
    if True in [R[r + dr][c + dc] == 0 for dr, dc in dir if (0 <= r+dr < N) and (0 <= c+dc < M)]:
        d = (d-1) % 4
        f_dr, f_dc = dir[d]
        if (0 <= r+f_dr < N) and (0 <= c+f_dc < M) and R[r+f_dr][c+f_dc] == 0:
            r += f_dr
            c += f_dc
    else:
        fdr, fdc = dir[d]
        bdr, bdc = -fdr, -fdc
        if not ( (0 <= r+bdr < N) and (0 <= c+bdc < M) ): break
        else:
            if R[r+bdr][c+bdc] == 1: break
            else:
                r = r + bdr
                c = c + bdc
print(ans)