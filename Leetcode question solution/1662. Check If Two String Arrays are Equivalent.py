#question

# 1662. Check If Two String Arrays are Equivalent


#Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

 


#solution 

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans=""
        ans1=""
        for i in word1:
            ans+=i
        for i in word2:
            ans1+=i
        if ans==ans1:
            return True
        return False
        