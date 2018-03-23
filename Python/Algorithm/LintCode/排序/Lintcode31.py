#31. 数组划分 

#给出一个整数数组 nums 和一个整数 k。划分数组（即移动数组 nums 中的元素），使得：

#所有小于k的元素移到左边
#所有大于等于k的元素移到右边
#返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。

#样例
#给出数组 nums = [3,2,2,1] 和 k = 2，返回 1.


class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < len(nums) and nums[left] < k: left += 1
            while nums[right] >= k and right >= 0: right -= 1
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        result = len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= k:
                result = i
                break
            
        return result


