#Question 
# 2016. Maximum Difference Between Increasing Elements

#problem statement
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] 
# (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.



#solution

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        x=0
        maxdifference=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                if i<j and nums[i]<nums[j]:
                    x=nums[j]-nums[i]
                    if maxdifference<x:
                        maxdifference=x
        return maxdifference
        
 