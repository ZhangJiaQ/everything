from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # n个括号的长度
        results = []
        result_str = ""
        self.backtrack(n, n, result_str, results)
        return results

    def backtrack(self, left, right, result_str, results):

        if left > right:
            return

        if left == 0 and right == 0:
            results.append(result_str)
        else:
            if left > 0:
                self.backtrack(left - 1, right, result_str + "(", results)
            if right > 0:
                self.backtrack(left, right - 1, result_str + ")", results)

if __name__ == '__main__':
    a = Solution()
    print(a.generateParenthesis(4))