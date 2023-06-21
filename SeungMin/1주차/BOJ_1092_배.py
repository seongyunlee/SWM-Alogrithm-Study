N = int(input())
crane = list(map(int, input().rstrip().split()))
M = int(input())
box = list(map(int, input().rstrip().split()))

if max(crane) < max(box):
    print(-1)

else:
    crane = sorted(crane, reverse=True)
    box = sorted(box, reverse=True)
    answer = 0
    while box:
        for i in crane:
            for j in range(len(box)):
                if i >= box[j]:
                    box.pop(j)
                    break
        answer += 1
    print(answer)
