def solution(user_id, banned_id):
    answer = 1
    canban = []
    banlist = []
    
    for i in banned_id:
        temp = []
        
        for j in user_id:
            if len(i) == len(j):
                for k in range(len(i)):
                    if i[k] != '*' and i[k] != j[k]:
                        break
                        
                    if k == len(i) - 1:
                        temp.append(j)
            
            else:
                continue
                
        canban.append(temp)
    
    banlist = list(canban[0])
    temp = []
    templist = []
    
    for i in range(1, len(canban)):
        for j in canban[i]:
            for k in banlist:
                if i == 1:
                    k = [k]
                else:
                    k = list(k)
                    
                if j not in k:
                    k.append(j)
                    temp.append(k)
        banlist = temp
        temp = []
    
    answer = []
    
    for i in range(len(banlist)):
        banlist[i] = sorted(banlist[i])
        if banlist[i] not in answer:
            answer.append(banlist[i])
    
    return len(answer)
            
