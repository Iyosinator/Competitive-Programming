t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    max_even = -1

    if b % 2 == 0:  
        if a % 2 == 0:
            max_even = a * (b // 2) + 2
        else: 
            if b % 4 == 0:
                max_even = a * (b // 2) + 2
    else:  
        if a % 2 == 1:
            max_even = a * b + 1

    print(max_even)
