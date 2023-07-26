import math

def solution(n, stations, w):
    answer = 0
    start = 0
    elec = 2 * w + 1 #station이 전파를 퍼뜨리는 길이
    
    for i in stations: #전파가 없는 부분들을 찾아서 길이를 더하는 제어문
        end = min(i - w - 2, n - 1) #해당 station이 전파를 퍼뜨리지 못하는 최대 지점
        answer += (math.ceil((end - start + 1)/elec)) # 
        start = end + elec + 1
    
    if start < n:
        answer += (math.ceil((n - start)/elec))
        
    return answer

# def solution(n, stations, w):

#     answer = 0
#     wifi = [0 for i in range(n)]
    
#     for i in stations:
#         for j in range(max(0, i - 1 - w), min(n, i + w)):
#             wifi[j] = 1 
    
#     count = 0
    
#     for i in range(n):
#         if wifi[i] == 0:
#             count += 1
#         else:
#             if count != 0:
#                 for j in range(i - (count), i):
#                     wifi[j] = 1 
#                 answer += 1
#             count = 0
            
#         if count == w * 2 + 1:
#             for j in range(i - (count), i + 1):
#                 wifi[j] = 1 
#             count = 0
#             answer += 1
#     if count != 0:
#         answer += 1
        
#     return answer