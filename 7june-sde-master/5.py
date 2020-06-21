value=[60, 40, 100, 120]
weight=[10, 40, 20, 30]
W=50    #total capacity
n=len(value)
d=[]

for i in range(len(weight)):
    d.append(value[i]/weight[i])
#bubble sort
for i in range(n):
    for j in range(0, n-i-1):
        if d[j] < d[j+1]:#sort by density
            d[j], d[j+1] = d[j+1], d[j]
            value[j], value[j+1] = value[j+1], value[j]
            weight[j], weight[j+1] = weight[j+1], weight[j]
#logic
fin=[]
for i in range(n):
    if(W-weight[i]>=0):
        W=W-weight[i]
        fin.append(value[i])
    elif(W-weight[i]<0):
        fin.append(float((value[i]/weight[i])*W))
        W=W-W
print(sum(fin))
