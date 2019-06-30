from copy import deepcopy, copy
"""
18. 子集 II
中文English
给定一个可能具有重复数字的列表，返回其所有可能的子集。

Example
样例 1：

输入：[0]
输出：
[
  [],
  [0]
]
样例 2：

输入：[1,2,2]
输出：
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Challenge
你可以同时用递归与非递归的方式解决么？

Notice
子集中的每个元素都是非降序的
两个子集间的顺序是无关紧要的
解集中不能包含重复子集

"""
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        result = []
        sol = []
        if not nums:
            return [[]]
    
        nums.sort()
        self.helper(nums, 0, sol, result)
        return result
        
    
    def helper(self, nums, i, sol, result):
        # 递归调用插入结果值
        subset = copy(sol)
        if subset not in result:
            result.append(subset)
    
        # 回溯算法，如果与上一个值相等则不添加到辅助数组中
        # 如果不相等则添加到辅助数组
        # 然后回溯添加到结果中
        for index in range(i, len(nums)):
            if (index != i) and (nums[i-1] == nums[i]):
                continue
            sol.append(nums[index])
            self.helper(nums, index+1, sol, result)
            sol.pop(-1) 