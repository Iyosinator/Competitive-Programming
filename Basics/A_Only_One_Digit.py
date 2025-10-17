t = int(input())


for i in range(t):
    n = int(input())
    smallest_digit = min(int(d) for d in str(n))
    print(smallest_digit)

