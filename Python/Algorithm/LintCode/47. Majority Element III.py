class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    48. 主元素 III
    给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的1/k。
    """
    def majorityNumber(self, nums, k):
        # write your code here
        
        # 思路 设置一个hashmap
        # 如果hashmap长度大于k 则hashmap内的所有值 -1 清除value为0的k
        # 继续添加
        hash_map = {}
        for d in nums:
            if d in hash_map:
                hash_map[d] += 1 
            else:
                if len(hash_map) > k - 1:
                    zero_list = []
                    for key in hash_map:
                        hash_map[key] -= 1
                        if hash_map[key] == 0:
                            zero_list.append(key)
                    for key in zero_list:
                        hash_map.pop(key)
                else:
                    hash_map[d] = 1
        # 遍历hashmap中的元素，取value最大的值
        
        target_num = 0
        target_count = 0
        for d in hash_map:
            if hash_map[d] >= target_count:
                target_num = d 
                target_count = hash_map[d]
        
        return target_num