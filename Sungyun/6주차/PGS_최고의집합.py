def solution(n, s):
    return [s//n+(1 if (n-i)<=s%n else 0) for i in range(n)] if n<=s else [-1]