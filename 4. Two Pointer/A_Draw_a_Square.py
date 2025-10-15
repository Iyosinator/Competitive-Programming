t = int(input())

for i in range(t):
    l,r,d,u = map(int,input().split())

    if l == r == d == u:
        print("Yes")
    else:
        print("No")