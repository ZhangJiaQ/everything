from typing import List


class Solution:

    """
    The gray code is a binary numeral system where two successive
    values differ in only one bit.
    Given an integer n representing the total number of bits in the code,
    return any sequence of gray code.
    A gray code sequence must begin with 0.
    """

    def grayCode(self, n: int) -> List[int]:
        seen = {0}

        def back_track(results):
            if len(results) == 2 ** n:
                print(1111111)
                return results
            for i in range(n):
                now = 1 << i ^ results[-1]
                if now in seen:
                    continue
                print(results, now)
                results.append(now)
                print(results, now)
                seen.add(now)
                if back_track(results):
                    return results
                results.pop()
                seen.remove(now)

        return back_track([0])


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(1))
    # print(s.grayCode(2))
    print(s.grayCode(3))
    # print(s.grayCode(4))
    # print(s.grayCode(5))
    # print(s.grayCode(6))