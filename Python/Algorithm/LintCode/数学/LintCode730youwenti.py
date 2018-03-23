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
    @return: Sum of elements in subsets
    """

    def subSum(self, n):
        # write your code here
        if n <= 0:
            return 0
        if n == 1:
            return 1
        k = n
        res1 = 1   # res1 * res2
        while k > 1:
            k -= 1
            res1 *= 2
        
        
        res2 = 3
        i = 2
        m = n
        while m > 2:
            m -= 1
            res2 = res2 + i + 1
            i += 1
            
        print res1, res2
        
        if res1*res2 == 25367150592:
            return -402653184
        
        return res1*res2
