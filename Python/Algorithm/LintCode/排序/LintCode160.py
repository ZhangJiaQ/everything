'''
寻找旋转排序数组中的最小值 II 

假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

数组中可能存在重复的元素。
'''


class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        len_num = len(nums)
        if len_num == 0:
            return nums
        if len_num == 1:
            return nums[0]
            
        for i in range(1, len_num):
            if nums[i] < nums[i-1]:
                nums = nums[i:] + nums[:i]
        
        print nums
        
        return nums[0]
            
        