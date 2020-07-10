from collections import defaultdict
d2=defaultdict(list)
class lpath:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        d2[self.a].append(self.b)
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    lpath(a,b)


#logic
li1=[]
li2=[]
for i,j in d2.items():
    li1.append(tuple(j))
x=[]
for i in li1:
    x.append(len(i))
x=sorted(x)
print(x[-1]+x[-2])
    
#sample input
'''
9
0 1
1 6
1 2
6 8
6 7
2 3
2 9
2 4
4 5
'''
