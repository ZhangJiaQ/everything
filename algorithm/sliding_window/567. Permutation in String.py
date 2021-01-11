class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 大概意思是，滑动窗口，非连续的 保持s2 不考虑顺序
        need_s1 = {}
        for i in s1:
            need_s1.setdefault(i, 0)
            need_s1[i] += 1
        word_count = {}
        left, right = 0, 0
        word_length = 0

        while right < len(s2):
            if s2[right] in need_s1:
                word_count.setdefault(s2[right], 0)
                word_count[s2[right]] += 1
                if word_count[s2[right]] == need_s1[s2[right]]:
                    word_length += 1
            right += 1



        return False


if __name__ == '__main__':
    s = Solution()
    a = "abc"
    b = "bbbca"
    assert s.checkInclusion(a, b) is True
