class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        '''
        407. 加一
        给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。
        
        该数字按照数位高低进行排列，最高位的数在列表的最前面。
        
        样例
        给定 [1,2,3] 表示 123, 返回 [1,2,4].
        
        给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
        '''
        digits[-1] += 1
        if digits[-1] >= 10:
            temp_int = 1
            digits[-1] = 0
        else:
            temp_int = 0
    
        for i in range(len(digits)-2, -1, -1):
            # temp_int = 1 需要进位
            if temp_int == 1:
                digits[i] += 1
            else:
                break
            if digits[i] >= 10:
                temp_int = 1
                digits[i] = 0
            else:
                temp_int = 0
        if temp_int:
            digits.insert(0, 1)
        return digits