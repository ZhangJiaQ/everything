from typing import List


class Solution:
    """
    因为可以买卖许多次，所以写出状态转移方程后化简数组即可
    """
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp_0 = 0
        dp_1 = -float("INF")
        for i in range(length):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_0 - prices[i], dp_1)
        return dp_0

if __name__ == '__main__':
    s = Solution()
    s.maxProfit([1,7,2,3,4])