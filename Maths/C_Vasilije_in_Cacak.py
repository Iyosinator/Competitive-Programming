t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    
    min_sum = k * (k + 1) // 2
    max_sum = k * (2 * n - k + 1) // 2

    print(min_sum,max_sum)
