#question

# 260. Single Number III

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



#solution 

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                ans.append(nums[i])
                if len(ans)==2:
                    return ans
        