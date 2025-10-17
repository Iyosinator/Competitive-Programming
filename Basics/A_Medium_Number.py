t = int(input())

for i in range(t):
    nums = list(map(int,input().split()))
   
    nums.remove(max(nums))
    nums.remove(min(nums))

    print(*nums)
    