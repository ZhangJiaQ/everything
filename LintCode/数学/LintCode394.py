'''
394. Coins in a Line 

There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?

思路 取到3则输 则第一名在硬币数量为3的倍数的情况下会输
'''


class Solution:
    """
    @param: n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n % 3 == 0:
            return False
        else:
            return True
