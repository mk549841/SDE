from collections import Counter
n,k=[int(x) for x in input().split()]
l=[]
s=''
[l.append(input()) for i in range(n)]
for i in range(k):
    l2=[]
    [l2.append(j[i])for j in l]    
    count=Counter(l2)
    val=count.values()
    ky=count.keys()
    k=max(val)
    h=chr(133)
    for j in ky:
        if count[j]==k:
            h=min(j,h)
    s=s+h
print(s)
