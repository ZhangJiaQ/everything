class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        '''
        413. 反转整数
        将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回 0 (标记为 32 位整数)。
        
        样例
        给定 x = 123，返回 321
        
        给定 x = -123，返回 -321
        '''
        if n < -2147483648 or n > 2147483647:
            return 0
        if n >= 0:
            n = int(str(n)[::-1])
            if n < -2147483648 or n > 2147483647:
                return 0
            else:
                return n
        else:
            n = int(str(n)[::-1][:-1]) * (-1)
            if n < -2147483648 or n > 2147483647:
                return 0
            else:
                return n