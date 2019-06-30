class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    45. Maximum Subarray Difference
    Given an array with integers.

    Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

    Return the largest difference.

    Example
    Example 1:

    Input:[1, 2, -3, 1]
    Output:6
    Explanation:
    The subarray are [1,2] and [-3].So the answer is 6.
    Example 2:

    Input:[0,-1]
    Output:1
    Explanation:
    The subarray are [0] and [-1].So the answer is 1.
    Challenge
    O(n) time and O(n) space.

    Notice
    The subarray should contain at least one number
    """
    def maxDiffSubArrays(self, nums):
        left_min, right_min, left_max, right_max = [0 for d in nums], [0 for d in nums], [0 for d in nums], [0 for d in nums]
    
        # 控制从左向右 计算最大子数组以及左小子数组
        sum, min_sum, max_sum, min_res, max_res = 0, 0, 0, float("inf"), float("-inf")
        for d in range(0, len(nums)):
            # 记录左到右数值
            sum += nums[d]
            # 记录最大子数组
            min_res = min(min_res, sum - max_sum)
            max_res = max(max_res, sum - min_sum)
            # 记录周期性最小值与最大值
            min_sum = min(min_sum, sum)
            max_sum = max(max_sum, sum)
            left_min[d] = min_res
            left_max[d] = max_res
    
        # 控制从左向右 计算最大子数组以及左小子数组
        sum, min_sum, max_sum, min_res, max_res = 0, 0, 0, float("inf"), float("-inf")
        for d in range(len(nums)-1, -1, -1):
            # 记录左到右数值
            sum += nums[d]
            # 记录最大子数组
            min_res = min(min_res, sum - max_sum)
            max_res = max(max_res, sum - min_sum)
            # 记录周期性最小值与最大值
            min_sum = min(min_sum, sum)
            max_sum = max(max_sum, sum)
            right_min[d] = min_res
            right_max[d] = max_res
    
        result = float("-inf")
        for d in range(len(nums)-1):
            result = max(result, abs(left_min[d] - right_max[d+1]), abs(left_max[d] - right_min[d+1]))
        return result