#Question : 78 Subsets

#problem statement
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


#solution

from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb=[]
        for i in range(len(nums)+1):
            comb += [list(j) for j in combinations(nums, i)]
        return comb
        