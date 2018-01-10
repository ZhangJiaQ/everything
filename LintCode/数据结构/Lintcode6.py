'''
6. 合并排序数组 

合并两个排序的整数数组A和B变成一个新的数组。

样例
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]
'''

class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A:
            return B
        if not B:
            return A
        
        len_A = len(A)
        len_B = len(B)
        i = 0
        j = 0
        res = []
        
        while i < len_A and j < len_B:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        
        while i < len_A:
            res.append(A[i])
            i += 1
            
        while j < len_B:
            res.append(B[j])
            j += 1
            
        return res