class Solution:
    """
    17. Subsets
    中文English
    Given a set of distinct integers, return all possible subsets.

    Example
    Example 1:

    Input: [0]
    Output:
    [
      [],
      [0]
    ]
    Example 2:

    Input: [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    Challenge
    Can you do it in both recursively and iteratively?
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
            # write your code here
        from queue import Queue
        from copy import deepcopy, copy
    
        nums_len = len(nums)
    
        nums_queue = Queue()
        result = []
    
        nums_queue.put([])
    
        while not nums_queue.empty():
            # 利用队列进行BFS 广度优先遍历 添加子数组
            temp_array = nums_queue.get()
            print(temp_array)
            result.append(temp_array)
    
            for i in range(nums_len):
                if (not temp_array) or (temp_array[-1] < nums[i]):
                    # 数组实际上是引用，所以要传递深拷贝
                    # deep_copy / copy
                    temp_array2 = copy(temp_array)
                    temp_array2.append(nums[i])
                    nums_queue.put(temp_array2)
    
        return result