t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a, x = [], n

    while x > 0:
        a.append(x % 3)
        x //= 3

    if sum(a) > k:
        print(-1)
        continue

    r = k - sum(a)
    for i in range(len(a)-1, 0, -1):
        if r == 0:
            break
        c = min(a[i], r//2)
        a[i] -= c
        a[i-1] += 3*c
        r -= 2*c

    s, m, j = 0, 1, 0
    
    for v in a:
        s += v * (3*m + (j*(m//3) if j>0 else 0))
        m *= 3
        j += 1

    print(s)
