#question
# 216. Combination Sum III

#problem statement :
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. 
# The list must not contain the same combination twice, and the combinations may be returned in any order.



#solution
from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        comb = []
        ans=[]
        array=[1, 2, 3,4,5,6,7,8,9]
        for i in range(len(array)+1):
            comb += [list(j) for j in combinations(array, i)]
        for i in comb:
            if len(i)==k:
                sum=0
                for j in range(len(i)):
                    sum+=i[j]
                if sum == n:
                    ans.append(i)
        return ans
        