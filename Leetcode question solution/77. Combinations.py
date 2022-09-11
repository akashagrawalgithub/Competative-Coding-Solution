#question

# 77. Combinations



# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.



#solution



from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        comb=[]
        for i in range(1,n+1,1):
            ans.append(i)
        for i in range(len(ans)+1):
            comb += [list(j) for j in combinations(ans, i)]
        ans.clear()
        for i in comb:
            if len(i)==k:
                ans.append(i)
        return ans