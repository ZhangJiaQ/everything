'''
608. 两数和-输入已排序的数组 
 Notice
给定一个已经按升序排列的数组，找到两个数使他们加起来的和等于特定数。
函数应该返回这两个数的下标，index1必须小于index2。注意返回的值不是 0-based。


解题思路：两个指针，存在重复数字的长度为N+1的最大为N的数组中一定存在环路

'''

class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i+1, j+1] if i < j else [j+1, i+1]
                
        
            