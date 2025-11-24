t = int(input())

for i in range(t):
    n = int(input())

    count = 0
    rep = 0
    for i in range(10):
        rep = rep *10 + 1

        for d in range(1,10):
            if d * rep <= n:
                count += 1
            else:
                break
    print(count)


'''


'''