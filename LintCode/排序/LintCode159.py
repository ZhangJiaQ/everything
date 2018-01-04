'''
159. Find Minimum in Rotated Sorted Array 
..
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
'''
class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if len(nums) == 0:
            return None
            
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                nums = nums[i:] + nums[:i]
                break
            
        return nums[0]
