s = input()

upper = 0
lower  = 0

for i in s:
    if i.isupper():
        upper += 1
    else:
        lower += 1

if lower >= upper:
    print(s.lower())
else:
    print(s.upper())

