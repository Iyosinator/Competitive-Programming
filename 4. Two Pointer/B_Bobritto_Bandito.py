t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    
    l_prime = max(l, -m)
    r_prime = l_prime + m
    
    print(l_prime, r_prime)