#question

# 1512. Number of Good Pairs


# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.



#solution

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j]:
                    count+=1
        return count