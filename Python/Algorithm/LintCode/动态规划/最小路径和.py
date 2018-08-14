class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        """
        110. 最小路径和
        给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。
        
        
        
        注意事项
        你在同一时间只能向下或者向右移动一步
        """
        # write your code here
        if len(grid) == 0:
            return 0
        temp = grid
        for k in range(len(temp)):
            for m in range(len(temp[k])):
                if k == 0 and m == 0:
                    pass
                elif k == 0:
                    temp[k][m] = temp[k][m-1] + temp[k][m]
                elif m == 0:
                    temp[k][m] = temp[k-1][m] + temp[k][m]
                else:
                    temp[k][m] = min(temp[k-1][m] + temp[k][m], temp[k][m-1] + temp[k][m])
        return temp[len(temp)-1][len(temp[0])-1]