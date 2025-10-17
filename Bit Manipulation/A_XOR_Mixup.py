t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = -1
    res = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            res ^= a[j]
        if res == a[i]:
            ans = a[i]
            break
    print(ans)