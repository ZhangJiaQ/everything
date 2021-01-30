from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        @param prices:
        @return:
        要有状态转移方程的思路
          首先需要定义出状态转移方程
          dp[-1][k][0] = 0
            解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
          dp[-1][k][1] = -infinity
            解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
          dp[i][0][0] = 0
            解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
          dp[i][0][1] = -infinity
            解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。
        """
        dp = [[0, 0] for _ in range(len(prices))]

        for index, price in enumerate(prices):
            if index == 0:
                dp[index][0] = 0
                dp[index][1] = -price
            else:
                dp[index][0] = max(dp[index - 1][0], price + dp[index - 1][1])
                dp[index][1] = max(dp[index - 1][1], -price)

        return max(dp[-1][0], dp[-1][1])


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([1, 2, 3, 4, 5])
