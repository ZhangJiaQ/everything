from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        不能连续抢劫两家
        @param nums: 每一家的价值
        @return:
        """
        memo = {}
        return self.dp(nums, 0, memo)

    def dp(self, nums, start, memo):
        if start in memo:
            return memo[start]
        if start >= len(nums):
            return 0
        res = max(
            # 抢劫，然后去下下家
            nums[start] + self.dp(nums, start+2, memo),
            # 不抢劫，然后去下家
            self.dp(nums, start+1, memo),
        )
        memo[start] = res
        return res


if __name__ == '__main__':
    _nums =  [1,2,3,1]
    s = Solution()
    print(s.rob(_nums))