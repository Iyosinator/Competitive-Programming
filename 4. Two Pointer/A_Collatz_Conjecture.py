t = int(input())
for i in range(t):
    k, x = map(int, input().split())
    
    for i in range(k):
        if (x - 1) % 3 == 0 and ((x - 1)//3) % 2 == 1:
            x = (x - 1) // 3
        else:
            x = x * 2 
    print(x)
