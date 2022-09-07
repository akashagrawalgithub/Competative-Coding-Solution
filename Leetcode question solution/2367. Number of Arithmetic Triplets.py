#Question

# 2367. Number of Arithmetic Triplets


# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.



#solution

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                        count+=1
        return count
        