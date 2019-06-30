class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        """
        75. 寻找峰值
        你给出一个整数数组(size为n)，其具有以下特点：

        相邻位置的数字是不同的
        A[0] < A[1] 并且 A[n - 2] > A[n - 1]
        假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。 
        """
        left = 0
        right = len(A) -1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
                return mid
            elif A[mid] > A[mid-1]:
                left = mid
            else:
                right = mid
                
        return 0
        
        