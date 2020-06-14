li=[]
t=[]
for _ in range(int(input())):
    m,n=map(int,input().split())
    for i in range(m):
        li.append(list(map(str,input().split())))
    max1=0
    '''for i in range(n):
        for j in range(n):
            if li[i][j]==1:
                if li[i][j+1]==1:
                    c+=1
                if li[i+1][j-1]==1 or li[i+1][j+1]==1:
                    c+=1'''
    for i in range(n):
        ind=[n1+1 for n1,x in enumerate(li[i]) if x=='1'] #finding pair(adjacent cell)
        t.append(ind)
    
    c=len(t[0])
    for i in range(len(t)-1):
        if t[i][0]-1 in t[i+1] or t[i][-1]+1 in t[i+1]:
            #print(t[i][0]-1,t[i][-1]+1,t[i+1])
            c+=len(t[i+1])
            #print(t[i])
        else:
            max1=max(c,max1)
            c=0
    print(max1)

#input        
                
'''
1
5 5
0 0 1 1 0
0 1 0 0 0
1 1 1 0 0
0 0 0 0 1
1 0 0 0 0'''
