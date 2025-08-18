t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    total_decreases = sum(max(ai - bi, 0) for ai, bi in zip(a, b))
    
    print(total_decreases + 1)
