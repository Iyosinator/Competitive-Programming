t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())

    if max(a,b,c) == (a+b+c) - max(a,b,c):
        print('YES')
    else:
        print('NO')
