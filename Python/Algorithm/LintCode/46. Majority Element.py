class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    46. Majority Element
    Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.
    """
    def majorityNumber(self, nums):
        # write your code here
        # 采用摩尔投票法
        # 摩尔投票法只能算出当前数量大于二分之一的数字 并不能算众数
        
        target_num, target_count = None, 0
        
        for d in nums:
            if d == target_num:
                # target_num出现次数+1
                target_count += 1
            elif target_count == 0:
                # target_num更换
                target_num = d 
            else:
                # 不是目标数字，投票数量-1  投票数量=0数字会变换
                target_count -= 1 
        
        return target_num