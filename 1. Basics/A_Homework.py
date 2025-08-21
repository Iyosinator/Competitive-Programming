from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()

    d = deque(a)

    for i in range(len(b)):
        if c[i] == "D":
            d.append(b[i])
        else:
            d.appendleft(b[i])
            
    result = ''.join(d)

    print(result)

