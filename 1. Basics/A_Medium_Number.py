t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())
    x = []
    x.append(a),x.append(b),x.append(c)
    x.sort()
    print(x[1])

    