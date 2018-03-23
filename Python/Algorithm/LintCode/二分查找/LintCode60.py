'''
60. Search Insert Position 
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

'''
class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        len_num = len(A)
        
        if len_num == 1:
            if A[0] < target:
                return 1
            else:
                return 0
        
        left = 0
        right = len_num - 1
        mid = 0
        
        while left <= right:
            mid = (left + right) // 2
            print mid
            
            if A[mid] == target:
                return mid
            if mid < len_num - 1 and mid > 0:
                if A[mid] < target and A[mid+1] > target:
                    return mid + 1
                if A[mid] > target and A[mid-1] < target:
                    return mid
            if A[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        if mid == 0:
            return 0
        if mid == len_num - 1:
            return len_num