n=int(input())
li=list(map(int,input().split()))
m=int(input())
t=0
li2=[]
for i in range(m):
    tar=int(input())
    for j in range(n):
        t=t+li[j]
        if t>=tar:
            print(j+1)
            t=0
            break
    if sum(li)<tar:
        print(-1)
        t=0
