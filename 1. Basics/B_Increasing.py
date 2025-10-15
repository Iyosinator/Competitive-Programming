t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    flag = True

    nums.sort()

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            flag = False

    if flag == True:
        print('YES')
    else:
        print('NO')