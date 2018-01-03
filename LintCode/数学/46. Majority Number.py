__author__ = 'Judge'
'''46. Majority Number 

Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

思路：字典与元组加数组操作

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
