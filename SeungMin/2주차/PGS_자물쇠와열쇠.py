import copy

def check(y, x, key, tempcheck, N, M):
    # key를 대입해보고 lock에 해당하는 부분이 모두 1이면 True를 반환하는 함수

    for i in range(M):
        for j in range(M):
            tempcheck[y + i][x + j] += key[i][j]

    for i in range(M - 1, N + M - 1):
        for j in range(M - 1, N + M - 1):
            if tempcheck[i][j] != 1:
                return False

    return True


def solution(key, lock):
    N, M = len(lock), len(key)
    tempkey = [[0] * len(key) for _ in range(len(key))]
    checkarr = [[0] * (N + (2 * M) - 2) for _ in range(N + (2 * M) - 2)]

    for i in range(M - 1, N + M - 1):  # checkarr 에 lock을 대입하는 제어문
        for j in range(M - 1, N + M - 1):
            checkarr[i][j] = lock[i - (M - 1)][j - (M - 1)]

    for i in range(4):  # 0, 90, 180, 270일 때 모두 돌려주기 위해 4번 반복
        for j in range(N + M - 1):
            for k in range(N + M - 1):
                tempcheck = copy.deepcopy(checkarr)
                if check(j, k, key, tempcheck, N, M):
                    return True

        for j in range(M):  # 행렬을 오른쪽으로 90도 회전하는 제어문
            for k in range(M):
                tempkey[k][M - 1 - j] = key[j][k]
        key = copy.deepcopy(tempkey)

    return False
