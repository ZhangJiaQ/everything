__author__ = 'Judge'
'''LintCode 723.
位旋转 -—— 旋转（或循环移位）是类似于移位的操作, 不同的是一端脱落的那一位会被放回到另一端
在左旋转中, 左端掉下来的那一位会放在右端
假设 n 用 8 位二进制来存. 对 n = 11100101 左旋转 3 位, 得到 n = 00101111 (左移3位, 原先的前3位放在末尾).
如果 n 用 16 位或 32 位二进制来存, 那么对 n (000…11100101)左旋转了之后会变成 (00..0011100101000).
在本问题中, 你可以假设 n 是用 32 位二进制来存的.
'''
class Solution:
    """
    @param: : a number
    @param: : digit needed to be rorated
    @return: a number
    """

    def leftRotate(self, n, d):
        # write code here
        binary_array = []
        
        while n > 1:
            binary_array.append(n%2)
            n //= 2
            
        binary_array.append(n)
        
        for i in range(len(binary_array), 32):
            binary_array.append(0)
        
        #字符串截取
        
        binary_array = binary_array[32-d:] + binary_array[:32-d]
        
        result = 0
        for index, value in enumerate(binary_array):
            if value == 1:
                result += pow(2, index)
        
        return result