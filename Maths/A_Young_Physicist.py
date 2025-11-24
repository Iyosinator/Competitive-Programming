t = int(input())

xt = 0
yt = 0
zt = 0

for i in  range(t):
    x,y,z = map(int,input().split())

    xt += x
    yt += y
    zt += z

if (xt,yt,zt) == (0,0,0):
    print('YES')
else:
    print('NO')

   

