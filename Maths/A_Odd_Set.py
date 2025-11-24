t = int(input())

for i in range(t):
    n = int(input())
    nums1 = list(map(int,input().split()))
    m = int(input())
    nums2 = list(map(int,input().split()))

    count = 0

    for i in range(n):
        for j in range(m):
            if nums1[i] + nums2[j] %2 != 0:
                count += 1
    print(count)