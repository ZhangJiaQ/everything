__author__ = 'Judge'
'''373. Partition Array by Odd and Even 

Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

'''
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        offset = 0
        for i, v in enumerate(nums):
            if v % 2 == 0:
                offset += 1
            else:
                nums[i], nums[i-offset] = nums[i-offset], nums[i]
                
        return nums
