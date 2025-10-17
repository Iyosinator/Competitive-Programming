t = int(input())

for i in range(t):
    a1,a2,b1,b2 = map(int,input().split())

    win_1 = 0 # Sunnet 
    win_2 = 0 # Slavic

    if ((a1 > b1) and (a2 > b2)) or ((a1 == b1) and (a2 > b2)) or ((a1 > b1) and (a2 == b2)) :
        win_1 += 1
    elif ((a1 < b1) and (a2 < b2)) or  ((a1 == b1) and (a2 < b2)) or  ((a1 < b1) and (a2 == b2)):
        win_2 += 1
    if ((a1 > b2) and (a2 > b1)) or ((a1 == b2) and (a2 > b1)) or ((a1 > b2) and (a2 == b1)):
        win_1 += 1
    elif ((a1 < b2) and (a2 < b1)) or ((a1 == b2) and (a2 < b1)) or ((a1 < b2) and (a2 == b1)): 
        win_2 += 1

    print(win_1* 2)

    
    

    
    
