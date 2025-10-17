t = int(input())

'''
n = x + y

y = x * (10^k)

n = x  + (x * (10^k))

x = n / 1+ 10^k

'''
for _ in range(t):
    n = int(input())
    x = [ n // (10**k + 1) for k in range(1, 20) if n % (10**k + 1) == 0]
    if x:
        x.sort()
        print(len(x))
        print(*x)
    else:
        print(0)
