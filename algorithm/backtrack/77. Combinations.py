from typing import List

class Solution:

    """
    执行用时：2756 ms, 在所有 Python3 提交中击败了5.10%的用户
    内存消耗：16.1 MB, 在所有 Python3 提交中击败了15.56%的用户
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Given two integers n and k, return all possible combinations
         of k numbers out of 1 ... n.
        You may return the answer in any order.
        @param n:
        @param k:
        @return:
        """
        # 1...n  k个数的全排列
        results = []
        n_list = range(1, n+1)
        result = []
        self.backtrack(k, results, n_list, result)
        return results

    def backtrack(self, k, results, n_list, result):
        print(result)

        if len(result) == k:
            results.append(list(result))
            return

        for d in n_list:
            if d in result:
                continue
            if len(result) > 0 and d < result[-1]:
                continue
            result.append(d)
            self.backtrack(k, results, n_list, result)
            result.pop(-1)

if __name__ == '__main__':
    a = Solution()
    print(a.combine(4, 2))
