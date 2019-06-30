class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        
        # 继续采用摩尔投票法
        # 好消息是大于1/3的数字只会有一个
        
        # 设置两个值 对两个值进行摩尔投票
        # 那么根据测算
        
        target1_num, target2_num, target1_count, target2_count = None, None, 0, 0
        
        for d in nums:
            # 投票后这两个就是出现次数前两位的数字
            if d == target1_num:
                target1_count += 1 
            elif d == target2_num:
                target2_count += 1 
            elif target1_count == 0:
                target1_num, target1_count = d, 1
            elif target2_count == 0:
                target2_num, target2_count = d, 1
            else:
                target1_count -= 1 
                target2_count -= 1
                
                
        target1_count, target2_count = 0, 0
        for d in nums:
            if d == target1_num:
                target1_count += 1
            elif d == target2_num:
                target2_count += 1
        return target1_num if target1_count >= target2_count else target2_num 