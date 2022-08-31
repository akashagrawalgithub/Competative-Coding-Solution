#Problem
# 1945. Sum of Digits of String After Convert


#problem statement:
# You are given a string s consisting of lowercase English letters, and an integer k.

# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.




#Solution

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=""
        array=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in s:
            x=array.index(i)
            y=x+1
            ans=ans+str(y)
        while(k>0):
            k=k-1
            sum=0
            for i in ans:
                sum=sum+int(i)
            if k>0:
                ans=str(sum)
            else:
                return int(sum)
            
        