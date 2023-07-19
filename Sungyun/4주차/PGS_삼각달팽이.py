import sys
sys.setrecursionlimit(10000)
A=None
def down(r,c,N):
    while r<len(A) and c<len(A[r]) and A[r][c]==0:
        A[r][c]=N
        N+=1
        r+=1
    right(r-1,c+1,N)
def right(r,c,N):
    while r<len(A) and c<len(A[r]) and A[r][c]==0:
        A[r][c]=N
        c+=1
        N+=1
    up(r-1,c-2,N)
def up(r,c,N):
    while r<len(A) and c<len(A[r]) and A[r][c]==0:
        A[r][c]=N
        c-=1
        r-=1
        N+=1
    if (r+2)<len(A) and (c+1)<len(A[r+2]) and A[r+2][c+1]==0:down(r+2,c+1,N)
def solution(n):
    global A
    A=[[0]*i for i in range(1,n+1)]
    down(0,0,1)
    D=[]
    for a in A:
        D+=a
    return D