t = int(input())

for i in range(t):
    n,q = map(int,input().split())
    steps = list(map(int,input().split()))
    queries = list(map(int,input().split()))

    prefix = []
    total = 0

    for h in steps:
        total += h
        prefix.append(total)

    

    for k in queries:
        height = 0

        for i in range(n):
            if steps[i] <= k:
                height = prefix[i]
            else:
                break
        
        print(height,end = ' ')
    print()