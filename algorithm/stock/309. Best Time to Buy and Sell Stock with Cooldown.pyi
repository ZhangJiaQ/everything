from typing import List


class Solution:
    """
    因为可以买卖许多次，所以写出状态转移方程后化简数组即可
    实际转移方程应该从index-2day算
    """
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp_0, dp_1, dp_2 = 0, -float("INF"), 0
        for index in range(length):
            temp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[index])
            dp_1 = max(dp_1, dp_2 - prices[index])
            dp_2 = temp
        return dp_0


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([1,7,2,3,4])