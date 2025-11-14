n, a, b, c = map(int, input().split())

ans = 0

for x in range(0, n//a + 1):       
    for y in range(0, n//b + 1):   
        rem = n - a*x - b*y
        if rem < 0:
            break
        if rem % c == 0:
            z = rem // c
            ans = max(ans, x+y+z)

print(ans)
