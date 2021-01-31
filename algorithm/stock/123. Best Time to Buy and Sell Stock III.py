from typing import List


class Solution:
    """
    只能交易两次
    列出状态转移方程后即可
    """
    def maxProfit(self, prices: List[int]) -> int:

        exchange_num = 2

        length = len(prices)
        
        # 设置状态转移方程
        dp_list = [[list([0, 0]) for _ in range(exchange_num + 1)] for _ in range(length)]

        for index in range(length):
            for exchange in range(exchange_num, 0, -1):
                if index - 1 == -1:
                    dp_list[index][exchange][0] = 0
                    dp_list[index][exchange][1] = -float("INF")
                dp_list[index][exchange][0] = max(dp_list[index - 1][exchange][0],
                                                  dp_list[index - 1][exchange][1] + prices[index])
                dp_list[index][exchange][1] = max(dp_list[index - 1][exchange - 1][0] - prices[index],
                                                  dp_list[index - 1][exchange][1])
        print(dp_list)
        return max([dp_list[-1][d][0] for d in range(exchange_num)])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))