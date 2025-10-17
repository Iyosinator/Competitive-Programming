t = int(input())

for _ in range(t):
    n = input().strip()
    total = sum(int(d) for d in n)
    
    if total % 9 == 0:
        print("YES")
        continue 
    
    count2 = n.count('2')
    count3 = n.count('3')
    
    found = False

    for x in range(min(count2, 8) + 1):
        for y in range(min(count3, 8) + 1):
            if (total + x*2 + y*6) % 9 == 0:
                print("YES")
                found = True
                break
            
        if found:
            break
    if not found:
        print("NO")