t = int(input())

for i in range(t):
    n,s = map(int,input().split())
    nums = list(map(int,input().split()))

    if sum(nums) > s:
        print(*nums)
    elif sum(nums) < s:
        d = s - sum(nums)
        if d == 1:
            zeros,ones,twos = nums.count(0),nums.count(1),nums.count(2)
            print(*( [0]*zeros + [2]*twos + [1]*ones ))
        else:
            print(-1)

    else:
        print(-1)
    

'''
if sum(nums) > s Bob Wins
if sum(nums) = s Alice Wins
if sum(nums) < s
    d = s- sum(nums)

    if d = 1 - Bob can do it by separating 0 and 1
    if d >= 2- Alice can do it no block

'''