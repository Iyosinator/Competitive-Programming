n, t = map(int, input().split())
s = list(input().strip())

for i in range(t):
    i = 0
    changed = False
    
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            s[i], s[i + 1] = s[i + 1], s[i]
            i += 2 
            changed = True
        else:
            i += 1
    if not changed:
        break

print("".join(s))
