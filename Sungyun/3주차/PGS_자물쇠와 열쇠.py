import numpy
def solution(key, lock):
    m=numpy.array(key,int)
    def solve(r,c):
        for i in range(len(lock)):
            for j in range(len(lock)):
                K=m[i-r][j-c] if (0<=i-r<len(key) and 0<=j-c<len(key)) else 0
                if int(K)==1 and lock[i][j]==1:
                    return False
                if int(K)==0 and lock[i][j]==0:
                    return False
        return True
    for _ in range(4):
        for i in range(-len(lock)+1,len(lock)):
            for j in range(-len(lock)+1,len(lock)):
                if solve(i,j):
                    return True
        m=numpy.rot90(m)
    return False