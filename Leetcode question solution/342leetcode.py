#Question 342 leetcode Day 1 of 100 Days of coding ...

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and log(n,4).is_integer()
        
# Time Complexity: O(1)

#follow me for such more such updates and solutions
