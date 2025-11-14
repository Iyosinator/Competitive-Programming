a = input().lower()
b = input().lower()

ans = 0
for i in range(len(a)):
    if ord (a[i]) > ord(b[i]):
        ans = 1
        break
    elif ord(a[i]) < ord(b[i]):
        ans = -1
        break

print(ans)
