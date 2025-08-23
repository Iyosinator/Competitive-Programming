t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())
    x = []
    x.append(a),x.append(b),x.append(c)
    x.sort()

    if x[-1] == x[0] + x[1]:
        print("YES")
    else:
        print("NO")