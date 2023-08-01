
def kkk(t):
    h,m = map(int,t.split(":"))
    return h*60+m
def solution(n, t, m, timetable):
    answer = '' 
    st = sorted([kkk(t) for t in timetable])
    wait = 0
    last = 540
    for bus in range(540,540+(n-1)*t+1,t):
        people = 0
        for now in range(wait,len(st)):
            if bus<st[now]:
                last = bus
                wait = now
                break
            else:
                people+=1
                if people==m:
                    wait = now+1
                    last = st[now]-1
                    break
        if people<m:
            last = bus
    return ':'.join([str(last//60).zfill(2),str(last%60).zfill(2)])