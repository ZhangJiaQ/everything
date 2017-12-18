__author__ = 'Judge'
'''LintCode 569.
569. 各位相加 
给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。
'''
class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        while num // 10 > 0:
            num = num // 10 + num % 10

        return num