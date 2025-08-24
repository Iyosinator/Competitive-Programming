t = int(input())

for _ in range(t):
    n, m, l, r = map(int, input().split())
    
    if m <= r:
        l_prime = 0
        r_prime = m
    else:
        r_prime = r
        l_prime = r - m
    
    print(l_prime, r_prime)
