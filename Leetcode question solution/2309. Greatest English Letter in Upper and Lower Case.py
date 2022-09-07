#question

# 2309. Greatest English Letter in Upper and Lower Case

# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears after a in the English alphabet.



#solution

class Solution:
    def greatestLetter(self, s: str) -> str:
        array=["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]
        for i in array:
            if i in s:
                x=i.lower()
                if x in s:
                    return i
        return ""
        