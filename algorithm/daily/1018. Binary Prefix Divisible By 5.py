from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        pre = 0
        for i in A:
            pre = (pre<<1)+i
            res.append(not pre%5)
        return res