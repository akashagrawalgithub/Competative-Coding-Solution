#Question
# 2180. Count Integers With Even Digit Sum

# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.


#solution


class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            if i<9 and i%2==0:
                count+=1
            else:
                sum=0
                for j in str(i):
                    sum+=int(j)
                if sum%2==0:
                    count+=1
        return count
                
        