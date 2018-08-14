class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        '''
        142. O(1)时间检测2的幂次
        用 O(1) 时间检测整数 n 是否是 2 的幂次。
        
        样例
        n=4，返回 true;
        
        n=5，返回 false.
        
        挑战
        O(1) time
        
        # 解释：使用位运算符，如16 二进制为 1 0000  15 为 二进制 0 1111  & 位运算为0
        '''
        # write your code here
        if n <= 0:
            return False
        if n&n-1 == 0:
            return True
        else:
            return False
