class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        '''
        109. 数字三角形
        给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。
        
        样例
        比如，给出下列数字三角形：
        
        [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。
        '''
        if len(triangle) == 0:
            return 0
        temp = triangle
        min_num = -2121221
        for k in range(len(temp)):
            if k == 0:
                min_num = temp[0][0]
            else:
                len_k = len(temp[k])
                for j in range(len(temp[k])):
                    if j == 0:
                        temp[k][0] = temp[k][0] + temp[k-1][0]
                    elif j < len_k - 1:
                        temp[k][j] = min(temp[k][j] + temp[k - 1][j], temp[k][j] + temp[k - 1][j-1])
                    else:
                        temp[k][j] = temp[k][j] + temp[k - 1][j - 1]
                print(temp[k])
                min_num = min(temp[k])
    
        return min_num