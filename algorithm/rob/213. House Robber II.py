from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        不能连续抢劫两家
        @param nums: 每一家的价值
        @return:
        """
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums):
        memo = {}
        return self.dp(nums, 0, memo)

    def dp(self, nums, start, memo):
        if start >= len(nums):
            return 0
        if start in memo:
            return memo[start]
        res = max(
            nums[start] + self.dp(nums, start+2, memo),
            self.dp(nums, start + 1, memo)
        )
        memo[start] = res
        return res


if __name__ == '__main__':
    _nums =  [1,2,3,1]
    s = Solution()
    print(s.rob(_nums))