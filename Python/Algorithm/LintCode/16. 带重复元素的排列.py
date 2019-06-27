



class Solution:
    """
    16. 带重复元素的排列
    给出一个具有重复数字的列表，找出列表所有不同的排列
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
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
            if temp_array not in all_result:
                all_result.append(temp_array)
        for index2, num in enumerate(nums):
            # 不为空进行循环递归调用
            # 将当前循环数据加入
            result.append(num)
            # 子数组用于递归
            kid_array = []
            for index, kid_num in enumerate(nums):
                if index != index2:
                    kid_array.append(kid_num)
            self.recursive_call(kid_array, result, all_result)
            result.pop()
        return