t = int(input())

for i in range(t):
    n = int(input())

    if n == 1:
        print(3)
    elif n & (n-1) == 0:
        print(n+1)
    elif n & (n-1) != 0:
        for i in range(32):
            if n & (1 << i):
                print(1 << i)
                break
