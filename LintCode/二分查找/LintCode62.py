'''
62. 搜索旋转排序数组 

假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

解题思路：二分法
'''
class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        
        offset = 0
        len_num = len(A)
        
        if len_num == 1:
            if A[0] == target:
                return 0
            else:
                return -1
        
        for i in range(1, len_num):
            if A[i] < A[i-1]:
                offset = i
                A = A[i:] +A[:i]
                
        left = 0
        right = len_num -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if A[mid] == target:
                return mid+offset if mid+offset<len_num else mid+offset-len_num
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid -1
                
        return -1