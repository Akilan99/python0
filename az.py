a,ji1=map(str,input().split())

ka1=0

if len(ma1)>len(ji1):

  a,ji1=ji1,a

i=0

while i<len(a):

  ka1+=(ord(ji1[i])-ord(a[i]))

  i+=1

for i in range(i,len(ji1)):

  ka1+=ord(ji1[i])-ord('b')+1

print(ka1)
