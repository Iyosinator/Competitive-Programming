t = int(input())

for i in range(t):
    n = int(input())
    paint = input().strip()

    '''
    l = s.index('B')
    r = s.rindex('B') 
    
    '''

    left = 0
    right = n-1


    while paint[left] == "W":
        left += 1
    while paint[right] == "W":
        right -= 1


    print(right-left+1)
