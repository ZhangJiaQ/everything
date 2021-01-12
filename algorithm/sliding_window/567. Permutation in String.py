class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 大概意思是，滑动窗口，非连续的 保持s2 不考虑顺序

        need_s1 = {}
        for i in s1:
            need_s1.setdefault(i, 0)
            need_s1[i] += 1
        window_num = len(need_s1.keys())
        start = 0
        temp_dict = {}
        for i in s2[start:start+window_num]:
            temp_dict.setdefault(i, 0)
            temp_dict[i] += 1
        while start + window_num <= len(s2):
            print(temp_dict, need_s1, start, s2[start: start + window_num], s2)
            for char in temp_dict.keys():
                need_s1_value = need_s1.get(char, 0)
                if temp_dict[char] != need_s1_value:
                    break
            if char in need_s1.keys():
                temp_dict_value = need_s1.get(char, 0)
                if temp_dict_value != need_s1[char]:
                    break
            else:
                return True
            if start + window_num >= len(s2):
                break
            temp_dict[s2[start]] -= 1
            temp_dict.setdefault(s2[start + window_num], 0)
            temp_dict[s2[start + window_num]] += 1
            start += 1

        return False


if __name__ == '__main__':
    s = Solution()
    a = "abc"
    b = "bbbca"
    assert s.checkInclusion(a, b) is True
    a = "ab"
    b = "eidbaooo"
    assert s.checkInclusion(a, b) is True
    a = "ab"
    b = "eidboaoo"
    assert s.checkInclusion(a, b) is False
    a = "a"
    b = "ab"
    assert s.checkInclusion(a, b) is True
    a = "hello"
    b = "ooolleoooleh"
    assert s.checkInclusion(a, b) is False