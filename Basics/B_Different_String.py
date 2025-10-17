t = int(input())
for i in range(t):
    word = input()
    
    if len(set(word)) == 1:
        print("NO")
        continue
    
    s = list(word)
   
    for i in range(1, len(s)):
        if s[i] != s[0]:
            s[0], s[i] = s[i], s[0]
            break
    
    print("YES")
    print(''.join(s))
