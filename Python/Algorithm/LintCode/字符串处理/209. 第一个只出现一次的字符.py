class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
		'''
		209. 第一个只出现一次的字符
		给出一个字符串，找出第一个只出现一次的字符。

		样例
		对于 "abaccdeff", 'b'为第一个只出现一次的字符.
		'''
        str_dict = {}
        for k in str:
            if k in str_dict:
                str_dict[k] += 1
            else:
                str_dict[k] = 1
        for k in str_dict:
            if str_dict[k] == 1:
                return k
        return ''
        