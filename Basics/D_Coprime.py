import math

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    last = [-1] * 1001
    for i, x in enumerate(arr):
        last[x] = i + 1 

    max_sum = -1
    for x in range(1, 1001):
        if last[x] == -1:
            continue
        for y in range(1, 1001):
            if last[y] == -1:
                continue
            if math.gcd(x, y) == 1:
                max_sum = max(max_sum, last[x] + last[y])
    
    print(max_sum)
