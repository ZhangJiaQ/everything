__author__ = 'Judge'
'''LintCode 428.
x的n次幂 
实现 pow(x,n)
'''
class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        if n < 0:
            res = 1
            if n < -100000:
                return 0.00
            while n < 0:
                res *= 1/x
                n += 1
            return res
        
        res = 1
        while n > 0:
            res *= x
            n -= 1
            
        return res
