class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        '''
        488. 快乐数
        写一个算法来判断一个数是不是"快乐数"。
        
        一个数是不是快乐是这么定义的：对于一个正整数，每一次将该数替换为他每个位置上的数字的平方和，然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。如果可以变为1，那么这个数就是快乐数。
        
        样例
        19 就是一个快乐数。
        
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
        '''
        try:
            i = 500 # 限制500次循环
            while n != 1:
                i = i -1
                if not i:
                    return False
                str_n = str(n)
                res_n = 0
                for k in str_n:
                    res_n += pow(int(k), 2)
                if n == res_n:
                    return False
                else:
                    n = res_n
            return True
        except:
            return False