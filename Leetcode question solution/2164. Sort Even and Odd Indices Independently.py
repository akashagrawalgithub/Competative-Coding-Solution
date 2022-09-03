#question

# 2164. Sort Even and Odd Indices Independently

# You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

# Sort the values at odd indices of nums in non-increasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
# Sort the values at even indices of nums in non-decreasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
# Return the array formed after rearranging the values of nums.



#solution
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        a=0
        b=0
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even[a])
                a+=1
            else:
                ans.append(odd[b])
                b+=1
        return ans