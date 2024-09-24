# Bruteforce 

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Sorting
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Time Complexity: O(nlogn)
# Space Complexity: O(1)


# Hash Set
def containsDuplicate(nums):
    hash_set = set()
    for i in nums:
        if i in hash_set:
            return True
        hash_set.add(i)
    return False    

# Time Complexity: O(n)
# Space Complexity: O(n)

# Hash Map
def containsDuplicate(nums):
    hash_map = {}
    for i in nums:
        if i in hash_map:
            return True
        hash_map[i] = 1
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

