'''
74. 第一个错误的代码版本 

代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。

你可以通过 isBadVersion 的接口来判断版本号 version 是否在单元测试中出错，具体接口详情和调用方法请见代码的注释部分。

解题思路：二分法
'''
"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if not n:
            return 0
        if n == 1:
            return 1 if SVNRepo.isBadVersion(1) else 0
        
        left = 1
        right = n
        mid = 0
        
        while left <= right:
            print 111
            mid = (left + right) // 2
            if SVNRepo.isBadVersion(mid):
                if not SVNRepo.isBadVersion(mid-1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1
                
        return mid