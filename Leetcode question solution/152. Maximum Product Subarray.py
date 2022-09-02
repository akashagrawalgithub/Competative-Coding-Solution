#question

# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.



#Solution

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        maxprod,minprod=ans,ans
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxprod,minprod=minprod,maxprod  
            maxprod=max(nums[i],maxprod*nums[i])
            minprod=min(nums[i],minprod*nums[i])
            ans=max(ans,maxprod) 
        return ans
        