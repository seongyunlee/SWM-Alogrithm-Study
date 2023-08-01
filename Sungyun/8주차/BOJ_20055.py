from collections import deque
N,K = map(int,input().split())
dur = list(map(int,input().split()))
pos = deque(range(2*N))
on = [False]*(2*N)
T = 0
B = 0
robot = deque()
while True:
    T+=1
    pos.appendleft(pos.pop())
    if on[pos[N-1]]: on[pos[N-1]]=False
    for idx in range(N-2,-1,-1):
        if not on[pos[idx]]: continue
        if (not on[pos[idx+1]]) and dur[pos[idx+1]]>0:
            dur[pos[idx+1]] -= 1
            if dur[pos[idx+1]]==0: B+=1
            if not idx==N-2:on[pos[idx+1]] = True
            on[pos[idx]] = False                
    if dur[pos[0]]>0:
        on[pos[0]] = True
        dur[pos[0]] -= 1
        if dur[pos[0]]==0: B+=1
    if B>=K:
        break
print(T)