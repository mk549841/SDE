def mukesh(a,b): 
    if(b==0): 
        return a 
    else: 
        return mukesh(b,a%b)
c=0
n=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li1=sorted(li1)
li2=sorted(li2)
for i in range(len(li1)):
    for j in range(len(li2)):
        if mukesh(li1[i],li2[j])!=1 and li1[i]<li2[j]:
            print(li1[i],li2[j])
            c+=1
print()
print('total edges',c)

