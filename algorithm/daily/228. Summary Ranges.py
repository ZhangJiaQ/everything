class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        start = nums[0]
        end = nums[0]

        for num in nums:
            if num == start and num == end:
                continue
            if num == end + 1:
                end = num
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                start = num
                end = num
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        return result