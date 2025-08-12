MOD = 998244353

def solve_case(n, k, s):
    zeros = [i for i, ch in enumerate(s, 1) if ch == '0']
    m = len(zeros)
    if m < k:
        return 0
    
    # dp[j][x] = number of ways to perform j operations with last zero at zeros[x]
    dp = [[0] * m for _ in range(k)]
    
    # Base case: one operation using zero at zeros[x]
    for x in range(m):
        dp[0][x] = 1
    
    for j in range(1, k):
        prefix_sum = 0
        for x in range(m):
            prefix_sum = (prefix_sum + dp[j-1][x]) % MOD
            dp[j][x] = prefix_sum
    
    # answer is sum of dp[k-1][x] for x in range(k-1, m)
    # because we need exactly k operations, and zeros used must be increasing sequence
    ans = 0
    for x in range(k - 1, m):
        ans = (ans + dp[k-1][x]) % MOD
    
    return ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(solve_case(n, k, s))
