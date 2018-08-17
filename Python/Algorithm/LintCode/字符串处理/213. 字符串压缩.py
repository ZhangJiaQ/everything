class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
	"""
		213. 字符串压缩
		设计一种方法，通过给重复字符计数来进行基本的字符串压缩。

		例如，字符串 aabcccccaaa 可压缩为 a2b1c5a3 。而如果压缩后的字符数不小于原始的字符数，则返回原始的字符串。

		可以假设字符串仅包括a-z的字母。

		样例
		str=aabcccccaaa 返回 a2b1c5a3
		str=aabbcc 返回 aabbcc
		str=aaaa 返回 a4
	"""
    def compress(self, st):
        # write your code here
        if not st:
            return ''
        if len(st) == 1:
            return st
        temp_str = st[0]
        temp_num = 1
        res = ''
        for s in st[1:]:
            if s == temp_str:
                temp_num += 1
            else:
                res = res + temp_str + str(temp_num)
                temp_str = s
                temp_num = 1
        if st[-1] == temp_str:
             res = res + temp_str + str(temp_num)
        if len(res) < len(st):
            return res
        else:
            return st