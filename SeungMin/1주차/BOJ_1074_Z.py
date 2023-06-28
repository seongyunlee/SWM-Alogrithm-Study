N, r, c = map(int, input().rstrip().split())
answer = 0
while N != 0:
    if (r % (2 ** N)) // (2 ** (N - 1)) == 0 and (c % (2 ** N)) // (2 ** (N - 1)) == 0:
        N -= 1
        continue
    elif (r % (2 ** N)) // (2 ** (N - 1)) == 0 and (c % (2 ** N)) // (2 ** (N - 1)) == 1:
        answer += (2 ** ((N - 1) * 2)) * 1

    elif (r % (2 ** N)) // (2 ** (N - 1)) == 1 and (c % (2 ** N)) // (2 ** (N - 1)) == 0:
        answer += (2 ** ((N - 1) * 2)) * 2

    else:
        answer += (2 ** ((N - 1) * 2)) * 3
    N -= 1

print(answer)
