equation = input()

ans = []

for i in equation:
    if i != "+":
        ans.append(int(i))

ans.sort()
print('+'.join(map(str,ans)))

