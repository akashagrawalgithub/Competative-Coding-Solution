#question

# 204. Count Primes

# Given an integer n, return the number of prime numbers that are strictly less than n.

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)