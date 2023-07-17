def solution(gems):
    gemtype = len(list(set(gems)))
    gemcount = {}
    start, end = 0, 0
    answer = [1, len(gems) + 1]
    
    while end < len(gems):
        if gems[end] not in gemcount: #end - 1까지 보지 못했던 gem일 때
            gemcount[gems[end]] = 1
        else:
            gemcount[gems[end]] += 1 
        
        if len(gemcount) == gemtype:
            while start < end + 1:
                if gemcount[gems[start]] > 1: #시작 위치에 있는 gem이 현재 범위에서 1개 이상이라면
                    gemcount[gems[start]] -= 1
                    start += 1
                    
                elif (answer[1] - answer[0]) > (end - start): #기존 최소였던 구간보다 길이가 적으면
                    answer = [start + 1, end + 1]
                    break
                else:
                    break
        end += 1
    return answer
                    
            
#     for i in range(len(gems)):
#         gemspot[gems[i]] = i + 1
        
#         if trigger == 1:
#             if ((i + 1) - min(gemspot.values())) < answer[1] - answer[0]:
#                 answer = [min(gemspot.values()), i + 1]
                
#         elif 0 not in gemspot.values():
#             trigger = 1
#             answer = [min(gemspot.values()), i + 1]
