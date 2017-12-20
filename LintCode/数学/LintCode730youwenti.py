'''
730. Sum of All Subsets

Given a number n, we need to find the sum of all the elements from all possible subsets of a set formed by first n natural numbers.

Given n = 2, return 6
Possible subsets are {{1}, {2}, {1, 2}}. Sum of elements in subsets
is 1 + 2 + 1 + 2 = 6

Given n = 3, return 24
Possible subsets are {{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
Sum of subsets is :
1 + 2 + 3 + (1 + 2) + (1 + 3) +
(2 + 3) + (1 + 2 + 3)
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
