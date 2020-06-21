a=[10,22,9,33,21,50,40,60]
c=1
for i in range(0,len(a)-1,1):
    if a[i]<a[i+1]:
        c+=1
print(c)
