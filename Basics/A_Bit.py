t = int(input())

counter = 0
for i in range(t):
    op = input()

    if op[0] == "+" or op[-1] == "+":
        counter +=1
    else:
        counter -=1

print(counter)
    