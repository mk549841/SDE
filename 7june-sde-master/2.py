from collections import OrderedDict
a=list(map(str,input()))
b=list(OrderedDict.fromkeys(a))
c=0
ma=-1
count=[]
alpha=[]
for i in b:
    for j in range(len(a)):
        if i ==a[j]:
            c+=1
    ma=max(c,ma)
    count.append(c)
    alpha.append(i)
    c=0
for i in count:
    if i==1:
        ind=count.index(1)
        count.pop(ind)
        alpha.pop(ind)
for i in alpha:
    print(i)
