'''
28. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

解题思路： 二分
'''

class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
        
        
        long = len(matrix[0])
        width = len(matrix)

        low = 0
        high = long * width - 1

        while low <= high:
            mid = (low+high) // 2
            print mid
            l = mid % long
            w = mid // long
            print l, w
            if matrix[w][l] == target:
                return True
            elif matrix[w][l] > target:
                high = mid - 1
            elif matrix[w][l] < target:
                low = mid +1
    
        return False