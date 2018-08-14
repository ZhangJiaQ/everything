class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        '''
        111. 爬楼梯
        假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
        
        样例
        比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法
        
        返回 3
        斐波那契函数非递归
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        temp = [1,1]
        for k in range(1, n):
            l = temp[-1] + temp[-2]
            temp.append(l)
            
        return temp[-1]