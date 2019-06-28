"""
32. 最小子串覆盖
中文English
给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的最短子串。

Example
例1:

输入:
""
""
输出:
""
例2:

输入:
"ADOBECODEBANC"
"ABC"
输出:
"BANC"
Challenge
要求时间复杂度为O(n)

Clarification
在答案的子串中的字母在目标字符串中是否需要具有相同的顺序？

——不需要。

Noti

"""

class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        """
        使用collection.Counter()对target计数
        然后双指针
        右指针向右移动，直到满足子串长度要求
        满足后左指针向右移动，直到不满足子串长度停止
        在左指针移动时不停的更新最小长度与子串
        """
        result = ""
        
        left, tarLen, minLen = 0, 0, float('INF')
        
        from collections import Counter
        counter_target = Counter(target)
        
        for index, value in enumerate(source):
            counter_target[value] -= 1
            if counter_target[value] >= 0:
                tarLen += 1
            
            while tarLen == len(target):
                # 计算当前符合的子串长度
                if minLen > index - left + 1:
                    minLen = index - left + 1
                    result = source[left: index+1]
                
                # 判断Counter 将数据返回给Counter内的元素
                counter_target[source[left]] += 1
                if counter_target[source[left]] > 0:
                    # 目前子串不符合target,停止遍历
                    tarLen -= 1 
                left += 1
                
        
        return result