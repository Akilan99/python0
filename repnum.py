n = int(input())
m = list(map(int,input().split()))
r = []
for i in range(len(m)):
    if m.count(m[i]) > 1:
        if m[i] not in r:
            r.append(m[i])
r.sort()
if len(r)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
