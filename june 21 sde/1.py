def mk(N, s):
    prime = [False] * (N+1)
    for i in range(2, N+1, 2):
        s[i] = 2
        for i in range(3, N+1, 2):
            if (prime[i] == False):
                s[i] = i
                for j in range(i, int(N / i) + 1, 2):
                    if (prime[i*j] == False):
                        prime[i*j] = True
                        s[i * j] = i
def generatePrimeFactors(N):
    s = [0] * (N+1)
    mk(N, s)
    print("Factor Power")
    curr = s[N]
    cnt = 1
    while (N > 1):
        N //= s[N]
        if (curr == s[N]):
            cnt += 1
            continue
        print(str(curr) + "\t" + str(cnt))
        curr = s[N]
        cnt = 1
N = 360
generatePrimeFactors(N)
