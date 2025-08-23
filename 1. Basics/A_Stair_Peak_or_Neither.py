t = int(input())

for i in range(t):
    a,b,c = map(str,input().split())


    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")