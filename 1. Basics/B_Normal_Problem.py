t = int(input())

for i in range(t):
    word = input()

    ans = []

    for i in range(len(word)):
        if word[i] == "p":
            ans.append("q")
        elif word[i] == "q":
            ans.append("p")
        else:
            ans.append("w")
    
    print(''.join(ans)[::-1])

    