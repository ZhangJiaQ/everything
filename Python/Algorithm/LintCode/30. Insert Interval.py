"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    30. Insert Interval
    中文English
    Given a non-overlapping interval list which is sorted by start point.

    Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

    Example
    Example 1:

    Input:
    (2, 5) into [(1,2), (5,9)]
    Output:
    [(1,9)]
    Example 2:

    Input:
    (3, 4) into [(1,2), (5,9)]
    Output:
    [(1,2), (3,4), (5,9)]
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        """
        1. 加入到一个数组内，按起始值进行排序
        2. 设置result数组，存入第一个区间元素
        3. for 循环剩余区间元素
            3.1 判断result数组最后一个区间元素的末尾值与for循环数组的第一个起始值
                如果for循环数组的第一个起始值 <= result 数组最后一个区间元素末尾值
                则证明有重叠 
                将result数组最后一个区间元素末尾值改为两者较大的值
            3.2 如果 > 则区间无重叠，正常append
        
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        
        result = [intervals[0]]
        
        for d in range(1, len(intervals)):
            len_num = len(result)
            
            if result[len_num-1].end >= intervals[d].start:
                # 执行重叠元素相加操作
                result[len_num-1].end = max(result[len_num-1].end, intervals[d].end)
            else:
                result.append(intervals[d])
                
        return result
        
        