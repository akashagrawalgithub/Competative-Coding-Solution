#question

# 2357. Make Array Zero by Subtracting Equal Amounts


# You are given a non-negative integer array nums. In one operation, you must:

# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.



#solution

import numpy as np
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while(1):
            if nums.count(0)!=len(nums):
                x=min(x for x in nums if x != 0)
                for i in range(len(nums)):
                    if nums[i]!=0:
                        nums[i]=nums[i]-x
                count+=1
            else:
                break
        return count
                
            
            
        