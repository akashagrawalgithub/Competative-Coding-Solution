#question

# 1385. Find the Distance Value Between Two Arrays


# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.




#solution


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans=0
        for i in range(len(arr1)):
            count=0
            for j in range(len(arr2)):
                x=abs(arr1[i]-arr2[j])
                if x>d:
                    count+=1
            if count==len(arr2):
                ans+=1
        return ans
            
        