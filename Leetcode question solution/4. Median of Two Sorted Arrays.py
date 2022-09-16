#Question


# 4. Median of Two Sorted Arrays


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).



#solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2!=0:
            return nums1[len(nums1)//2]
        else:
            x=(nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2
            return x
        