k=int(input())
s=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,k):
    s*=10
    s+=int(array[a])
print(s)
