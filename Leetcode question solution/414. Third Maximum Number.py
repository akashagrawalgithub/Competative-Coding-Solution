#Question
# 414. Third Maximum Number

#Given an integer array nums, return the third distinct 
# maximum number in this array. If the third maximum does not exist, return the maximum number.

#solution 
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)<3:
            return max(nums)
        else:
            return nums[2]
        