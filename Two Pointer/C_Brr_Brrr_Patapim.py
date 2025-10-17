t = int(input())

for _ in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    p = [0] * (2 * n + 1)
    seen_values = set()
    
    for i in range(n):
        for j in range(n):
            val = grid[i][j]
            p[i + j + 2] = val
            seen_values.add(val)
    
    p1 = 0
    for i in range(1, 2 * n + 1):
        if i not in seen_values:
            p1 = i
            break
            
    ans = [p1]
    for i in range(2, 2 * n + 1):
        ans.append(p[i])
        
    print(*ans)