n = int(input())

cycle = [8,4,2,6]

if n == 0:
    print(1)
else:
    print(cycle[(n-1) % 4])