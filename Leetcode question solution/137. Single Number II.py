#question
# 137. Single Number II

# Given an array of integers, every element appears three times except for one, which appears exactly once. 
# Find that single one.



#solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]
        