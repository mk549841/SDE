for _ in range(int(input())):
        a,b=map(int,input().split())
        c,d=map(str,input().split())
        x=min(a,b)
        y=max(a,b)
        t=''
        c1=0
        for i in range(x,y):
                c1+=1
                t=t+c+d
        print(c1+1,t[c1-1])
        
        
        
        

