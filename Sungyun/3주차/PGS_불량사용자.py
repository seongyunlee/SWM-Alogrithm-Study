from itertools import combinations

B=None
def match(name,mask):
    if len(name)!=len(mask):return False
    return all([mask[i] in [name[i],'*'] for i in range(len(name))])
def dfs(pick,idx,banned):
    if idx==len(pick):return True
    for i in range(len(banned)):
        if banned[i] and match(pick[idx],B[i]):
            n_banned=list(banned)
            n_banned[i]=False
            if dfs(pick,idx+1,n_banned):return True
    return False
def solution(user_id, banned_id):
    answer = 0
    global B
    B=banned_id
    for pick in combinations(user_id,len(B)):
        if dfs(pick,0,[True]*len(banned_id)):
            answer+=1
    return answer