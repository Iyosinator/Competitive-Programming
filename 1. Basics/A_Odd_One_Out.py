t = int(input())

for i in range(t):
    a,b,c = map(str,input().split())

    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(b)