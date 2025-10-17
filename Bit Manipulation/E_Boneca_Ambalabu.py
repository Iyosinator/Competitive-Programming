t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * 30



    for x in arr:
        for b in range(30):
            if x & (1 << b):
                cnt[b] += 1
    #print(cnt)
    best = 0
    for a in arr:
        s = 0
        for b in range(30):
            
            if (a & (1 << b)):
                s += (n - cnt[b]) 
            else:
                cnt[b] << b
        
        best = max(best, s)

    print(best)