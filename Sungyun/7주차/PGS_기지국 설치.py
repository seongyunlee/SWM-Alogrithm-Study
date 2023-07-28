from math import ceil
def solution(n, stations, W):
    answer=0
    last = 0
    for i in range(len(stations)):
        if stations[i]-W>last:
            answer+=ceil(((stations[i]-W)-last-1)/(2*W+1))
        last=stations[i]+W
    if last<n: answer+=ceil((n-last)/(2*W+1))
    return answer