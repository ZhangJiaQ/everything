from typing import List


class Solution:
    """
    因为可以买卖许多次，所以写出状态转移方程后化简数组即可
    直接在成本端+2
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        dp_0, dp_1 = 0, -float("INF")
        for index in range(length):
            dp_0 = max(dp_0, dp_1 + prices[index])
            dp_1 = max(dp_1, dp_0 - (prices[index] + fee))

        return dp_0


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))