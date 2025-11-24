t = int(input())


for i in range(t):
    n = input().strip()
    col = n[0]
    row = n[1]

    for r in '12345678':
        if r != row:
            print(col + r)

    for c in 'abcdefgh':
        if c != col:
            print(c + row)

'''
a8 -> b-h8, a1-7



'''

