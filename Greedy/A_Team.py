t = int(input())
solved = 0


for i in range(t):
    petya,vasya,tonya = map(int,input().split())
    total = petya + vasya + tonya
    
    if total > 1:
        solved += 1
    
print(solved)