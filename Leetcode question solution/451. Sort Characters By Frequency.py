#question

# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

#solution

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        ans=[]
        for i in s:
            ans.append(i)
        result = [item for items, c in Counter(ans).most_common()for item in [items] * c]
        return result
        