a=int(input())
p=list(map(int,input().split()))
d=[]
for i in range(len(p)):
    if i==p[i]:
        d.append(i)
        
if len(d)>=1:
    print(*d)
else:
    print(-1)
