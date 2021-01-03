from typing import List
from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        result = []
        temp = ["."] * n
        for _ in range(n):
            result.append(list(temp))

        self.backtrack(result, results, 0)

        for result in results:
            for i, v in  enumerate(result):
                result[i] = "".join(v)


        return results

    def backtrack(self, result, results, length):
        if length == len(result):
            _result = deepcopy(result)
            results.append(_result)
            return

        for i in range(len(result)):
            if not self.is_valid(i, length, result, len(result)):
                continue
            result[length][i] = "Q"
            # print(result)
            self.backtrack(result, results, length + 1)
            result[length][i] = "."

    def is_valid(self, i, length, result, n):
        # 其实这个是从上向下写的，所以只需要验证 左上 右上 上方有没有不合适的
        recurise_time = 1
        length -= 1
        while length >= 0:
            if result[length][i] == "Q":
                return False
            if i + recurise_time < n and result[length][i + recurise_time] == "Q":
                return False
            if i - recurise_time >= 0 and result[length][i - recurise_time] == "Q":
                return False
            recurise_time += 1
            length -= 1

        return True


if __name__ == '__main__':
    a = Solution()
    print(a.solveNQueens(4))

