x = list(map(int, input().split()))
x.sort()
s = x[3]
a = s - x[2]
b = s - x[1]
c = s - x[0]
print(a, b, c)
