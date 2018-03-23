'''
61. Search for a Range 
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

'''
class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        result = [-1, -1]
        len_num = len(A)
        
        left = 0
        right = len_num - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                print mid
                l ,r = mid, mid
                result[0] = l
                result[1] = r
                while l >= 0 and A[l] == target:
                    result[0] = l
                    l -= 1
                while r < len_num and A[r] == target:
                    result[1] = r
                    r += 1
                break
                
                
                
        return result