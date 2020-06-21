def MinOperation(a, n, k):
    result = 0
    for i in range(n):
        if (a[i] != 1 and a[i] > k):
            result = (result + min(a[i] % k,k - a[i] % k))
        else:
            result = result + k - a[i]
            return result 
arr=list(map(int,input().split())) 
n = len(arr)
k =int(input())
print(MinOperation(arr, n, k))
