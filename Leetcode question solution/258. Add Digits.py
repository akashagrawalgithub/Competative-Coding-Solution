#question


# 258. Add Digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


#solution



class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        while(num>9):
            num=num%10 + num//10
        return num
        