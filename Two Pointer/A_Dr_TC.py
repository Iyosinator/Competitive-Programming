t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    cnt1 = s.count('1')
    ans = (n - 2) * cnt1 + n
    
    print(ans)
