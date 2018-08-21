class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        '''
        397. 最长上升连续子序列
        给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）
        
        样例
        给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.
        
        给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.
        
        挑战
        使用 O(n) 时间和 O(1) 额外空间来解决
        '''
        if not A:
            return 0
        list_bigger = 1
        list_lower = 1
        res = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                list_bigger += 1
                list_lower = 1
            else:
                list_lower += 1
                list_bigger = 1
            res = max(list_bigger, list_lower, res)
        return res