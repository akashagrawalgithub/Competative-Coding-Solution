#Question
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

#Time complexity :- O(n)