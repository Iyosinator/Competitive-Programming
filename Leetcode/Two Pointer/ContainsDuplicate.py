
# Bruteforce Approach

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Sorting Approach

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
# Time Complexity: O(nlogn)
# Space Complexity: O(1)


# Hash Set Approach

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setholder = set()
        for num in nums:
            if num in setholder:
                return True
            setholder.add(num)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
