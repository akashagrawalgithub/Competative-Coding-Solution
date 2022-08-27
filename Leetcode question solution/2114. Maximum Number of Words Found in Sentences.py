#problem 2114. Maximum Number of Words Found in Sentences

#problem statement

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.


#solution

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=[]
        for i in sentences:
            x=len(i.split())
            ans.append(x)
        return max(ans)
        

 