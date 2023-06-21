N,_=int(input()),input()
B=set(input().split())
ans=abs(N-100)
now = -1
if all([str(i) in B for i in range(1,10)]):
    print(min(N+1,ans))
    exit()
while True:
    now+=1
    if not all([n not in B for n in str(now)]):continue
    ans=min(ans,abs(now-N)+len(str(now)))
    if now>=500000:break
print(ans)