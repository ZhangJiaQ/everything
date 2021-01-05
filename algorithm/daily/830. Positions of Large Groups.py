class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []
        large_targe = 3
        result = []
        letter = s[0]
        temp = [0, 0]
        for index in range(1, len(s)):
            if s[index] == letter:
                temp[1] = index
            else:
                if temp[1] - temp[0] >= 2:
                    result.append(list(temp))
                temp[0] = index
                letter = s[index]
        if temp[1] - temp[0] >= 2:
            result.append(list(temp))
        return result

