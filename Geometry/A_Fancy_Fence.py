t = int(input())

for i in range(t):
    a = int(input())

    n = 360 / (180- a)

    if n%1 == 0:
        print('YES')
    else:
        print('NO')