t = int(input())

for i in range(t):
    n = int(input())
    print((1 << (n.bit_length() - 1)) - 1)