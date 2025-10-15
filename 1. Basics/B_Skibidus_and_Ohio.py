t = int(input())

for i in range(t):
    word = input()
    count = 0


    for i in range(1,len(word)):
        if word[i-1] == word[i]:
            count += 1
       

    if count == 0:
        print(len(word))
    else:
        print(1)
