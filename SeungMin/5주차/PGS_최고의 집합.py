# from itertools import combinations_with_replacement

def solution(n, s):
    num = s // n
    diff = s - (num * n)
    arr = [num] * n 
    if num == 0:
        return [-1]
    
    for i in range(diff):
        arr[-(i + 1)] += 1
        
    return arr
#     answer = []
#     maxmulti = 0
#     arr = []
#     num = [i for i in range(1, s - n + 2)]
#     if not num:
#         return [-1]
    
#     for i in list(combinations_with_replacement(num, n)):
#         if sum(i) == s:
#             arr.append(i)
    
#     for i in arr:
#         temp = 1
#         for j in i:
#             temp *= j
        
#         if maxmulti < temp:
#             maxmulti = temp
#             answer = i
            
#     return answer
