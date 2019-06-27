



class Solution:
    """
    15. 全排列
    给定一个数字列表，返回其所有可能的排列。
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        # 递归调用下面方法
        result = []
        all_result = []
        self.recursive_call(nums, result, all_result)
        return all_result
    
    def recursive_call(self, nums, result, all_result):
        # 第一步先判断是否为空
        if not nums:
            # 为空加入最终结果数组
            # 不进行下面那一组声明，直接append result会导致所以result为空，因为数组存的是对象的引用
            temp_array = []
            for i in result:
                temp_array.append(i)
            all_result.append(temp_array)
        for num in nums:
            # 不为空进行循环递归调用
            # 将当前循环数据加入
            result.append(num)
            # 子数组用于递归
            kid_array = []
            for kid_num in nums:
                if kid_num != num:
                    kid_array.append(kid_num)
            self.recursive_call(kid_array, result, all_result)
            result.pop()
        return