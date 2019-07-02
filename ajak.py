b1=int(input())
b2=list(map(int,input().split()))
a1=0
for x in range(len(b2)-2):
    for y in range(x+1,len(b2)-1):
        for z in range(y+1,len(b2)):
            if b2[x]<b2[y]<b2[z] and x<y<z:
                a1=a1+1
print(a1)
