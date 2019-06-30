class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        """
        思路 滑动窗口
        42. Maximum Subarray II
        Given an array of integers, find two non-overlapping subarrays which have the largest sum.
        The number in each subarray should be contiguous.
        Return the largest sum.

        Example
        Example 1:

        Input:
        [1, 3, -1, 2, -1, 2]
        Output:
        7
        Explanation:
        the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
        Example 2:

        Input:
        [5,4]
        Output:
        9
        Explanation:
        the two subarrays are [5] and [4].
        Challenge
        Can you do it in time complexity O(n) ?

        Notice
        The subarray should contain at least one number
        """
        left, right = [0 for d in range(len(nums))], [0 for d in range(len(nums))]

        # 从左向右的最大子数组
        res, min_sum, sum = float("-inf"), 0, 0
        for index, value in enumerate(nums):
            # sum记录从左向右子数组的和
            sum += value
            # res记录从左向右最大子数组的和
            res = max(res, sum-min_sum)
            # min_sun记录从左向右最小子数组的和，用于res计算
            min_sum = min(min_sum, sum)
            left[index] = res
    
        # 从右向左的最大子数组
        res, min_sum, sum = float("-inf"), 0, 0
        for index in range(len(nums)-1, -1, -1):
            # sum记录从右向左子数组的和
            sum += nums[index]
            # res记录从左向右最大子数组的和
            res = max(res, sum-min_sum)
            # min_sun记录从左向右最小子数组的和，用于res计算
            min_sum = min(min_sum, sum)
            right[index] = res
    
        # 从左向右计算出最大子数组
        # 子数组有可能由从左向右子数组 与 从右向左子数组叠加而成
        # 遍历后可以求出  从左至右的最大子数组的和与从右至左的最大子数组的和相加的值
        res = float("-inf")
        for index in range(len(nums)-1):
            res = max(res, left[index] + right[index+1])
        return res  
