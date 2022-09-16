#question

# 2351. First Letter to Appear Twice



# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:

# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.



#solution

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans=""
        for i in s:
            if i in ans:
                return i
            else:
                ans=ans+i
        
 