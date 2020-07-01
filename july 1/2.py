li=[10,5,20,5,10,10,30]
k=2
r=[]
s=set(li)
for i in s:
        if li.count(i)>=k:
                r.append(i)
for i in r:
        print(i,end=' ')
