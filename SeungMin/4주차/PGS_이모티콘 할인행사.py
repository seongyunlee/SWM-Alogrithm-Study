import itertools

def plusjoin(user, dis, emoticons, tempplus):
    tempsum, tempcount = 0, 0
    
    for j in range(len(dis)):
        if user[0] <= dis[j]:
            tempsum += emoticons[j] * (100 - dis[j]) // 100
            tempcount += 1
            if tempsum >= user[1]:
                tempsum = 0
                tempplus += 1
                return(tempsum, tempplus)
    return(tempsum, tempplus)
    
def solution(users, emoticons):
    rate = [10, 20, 30, 40]
    discount = list(itertools.product(rate, repeat = len(emoticons)))
    answer = [0, 0]
    
    for dis in discount:
        dis = list(dis)
        tempplus = 0
        tempsell = 0
        for i in users:
            tempsum, tempplus = plusjoin(i, dis, emoticons, tempplus)
            tempsell += tempsum
        
        if tempplus > answer[0]:
            answer[0] = tempplus
            answer[1] = tempsell
            
        elif tempplus == answer[0]:
            if tempsell >= answer[1]:
                answer[1] = tempsell
        

    return answer