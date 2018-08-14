 class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        sum = 0
        min_sum = nums[0]
        prev_sum = 0
        for num in nums:
            sum += num
            if sum  < min_sum:
                min_sum = sum
            if sum > 0:
                sum = 0
        return min_sum