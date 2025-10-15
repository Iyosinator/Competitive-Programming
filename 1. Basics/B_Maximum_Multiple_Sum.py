t = int(input())
for i in range(t):
    n = int(input())
    maxsum = 0
    ans = 0

    for x in range(2, n + 1):
        total = 0
        multiple = x

        while multiple <= n:
            total += multiple
            multiple += x
        if total > maxsum:
            maxsum = total
            ans = x
    print(ans)
