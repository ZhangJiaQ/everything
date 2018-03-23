#Sort Colors 

#Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

#Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].


class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []
        left  = 0
        p0 = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 2:
                nums[left], nums[right] =  nums[right], nums[left]
                right -= 1
            elif nums[left] == 0:
                nums[left], nums[p0] = nums[p0], nums[left]
                left += 1
                p0 += 1
            else:
                left += 1
