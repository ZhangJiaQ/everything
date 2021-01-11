class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need_words_count = {}
        for word in t:
            need_words_count.setdefault(word, 0)
            need_words_count[word] += 1
        now_word_count = {}

        left, right = 0, 0
        result = ""
        match_length = 0
        min_length = float("INF")
        start = 0
        while right < len(s):
            # 向右找到符合要求的
            if s[right] in need_words_count:
                now_word_count.setdefault(s[right], 0)
                now_word_count[s[right]] += 1
                if now_word_count[s[right]] == need_words_count[s[right]]:
                    match_length += 1

            # 判断是否可以左边滑动
            while match_length == len(need_words_count.keys()):
                if right - left < min_length:
                    start = left
                    min_length = right - left
                if s[left] in now_word_count:
                    if now_word_count[s[left]] - need_words_count[s[left]] == 0:
                        break
                    else:
                        now_word_count[s[left]] -= 1
                        left += 1
                else:
                    left += 1
            right += 1
        if min_length == float("INF"):
            return ""
        else:
            return s[start:start + min_length + 1]



if __name__ == '__main__':
    s = Solution()
    a = "aa"
    b = "aa"
    print(s.minWindow(a, b))
    print(s.minWindow("a", "a"))
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("cabwefgewcwaefgcf", "cae"))
