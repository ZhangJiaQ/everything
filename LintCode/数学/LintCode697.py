'''
697. Check Sum of Square Numbers

Given a integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example
Given n = 5
Return true // 1 * 1 + 2 * 2 = 5

Given n = -5
Return false
'''


class Solution:
    """
    @param: : the given number
    @return: whether whether there're two integers
    """

    def checkSumOfSquareNumbers(self, num):
        # write your code here

        maxs = 0
        while maxs * maxs < num:
            maxs += 1

        low = 0
        high = maxs

        result = 0

        while low <= high:
            if low * low + high * high == num:
                return True
            elif low * low + high * high < num:
                low += 1
            else:
                high -= 1

        return False
