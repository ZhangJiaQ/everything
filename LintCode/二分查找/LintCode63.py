'''
63. 搜索旋转排序数组 II 

跟进“搜索旋转排序数组”，假如有重复元素又将如何？

是否会影响运行时间复杂度？

如何影响？

为何会影响？

写出一个函数判断给定的目标值是否出现在数组中。

样例

给出[3,4,4,5,7,0,1,2]和target=4，返回 true

解题思路：二分法
'''
class Solution:
    """
    @param: A: an integer ratated sorted array and duplicates are allowed
    @param: target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        len_num = len(A)
        
        if not A:
            return False
        if len_num == 1:
            if A[0] == target:
                return True
            else:
                return False
        
        for i in range(1, len_num):
            if A[i] < A[i-1]:
                A = A[i:] + A[:i]
                
        left = 0
        right = len_num -1
        
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return True
            elif A[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False