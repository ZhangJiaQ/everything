"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

920. 会议室
给定一系列的会议时间间隔，包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，确定一个人是否可以参加所有会议。

样例
给定区间=[[0,30]，[5,10]，[15,20]]，返回false。
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        # intervals 是一个二维数组
        if not intervals:
            return True

        # 所有时间表按开始时间排好序
        intervals = sorted(intervals, key = lambda x: x.start)
        
        # 查询是否有交集，也就是用本次会议的结束时间与下次会与的开始时间进行比对
        start_time = intervals[0].start
        end_time = intervals[0].end
        
        for index,timeline in enumerate(intervals):
            if index == 0:
                continue
            start_time = timeline.start
            if start_time < end_time:
                return False
            else:
                end_time = timeline.end
        
        return True