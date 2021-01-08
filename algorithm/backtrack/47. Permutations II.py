from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        result = []
        result_index = []
        nums.sort()
        self.dfs(nums, results, result, result_index)
        return results

    def dfs(self, nums, results, result, result_index):
        if len(result) == len(nums) :
            results.append(list(result))
            return

        for index, value in enumerate(nums):
            if index in result_index:
                continue
            # index 1    result_index [2, ] value 1
            if index > 0 and index - 1 not in result_index and nums[index - 1] == nums[index]:
                continue

            result_index.append(index)
            result.append(value)
            self.dfs(nums, results, result, result_index)
            result_index.pop()
            result.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 3]))