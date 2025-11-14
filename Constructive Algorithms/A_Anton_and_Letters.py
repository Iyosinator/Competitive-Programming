letters =  input()

x = []

for i in letters:
    if i.islower():
        x.append(i)

print(len(set(x)))

