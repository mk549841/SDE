a,b=map(str,input().split())
for i in range(int(b)-1):
        if a[-1]!='0':
                a=str(int(a)-1)
        if a[-1]=='0':
                a=a[:-1:]
print(int(a))

                
        
