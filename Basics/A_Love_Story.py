t = int(input())

for i in range(t):
    s = input()
    x = ['c', 'o', 'd', 'e', 'f', 'o', 'r', 'c', 'e', 's']
    y = list(s)
    counter = 0

    for i in range(len(x)):
        if x[i] != y[i]:
            counter += 1
    print(counter)
    


