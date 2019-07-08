p=int(input())
d=[int(i) for i in input().split()]
m=0
for k in range(p):
   for j in range(k):
      if d[j]<d[k]:
         m+=d[j]
print(m) 
