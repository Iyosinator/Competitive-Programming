t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())

    if (a+b) >= 10 or (c+b) >= 10 or (a+c) >= 10:
        print("YES")
    else:
        print("NO")