class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
		'''
		422. 最后一个单词的长度
		给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

		如果不存在最后一个单词，请返回 0 。

		样例
		给定 s = "Hello World"，返回 5。

		注意事项
		一个单词的界定是，由字母组成，但不包含任何的空格。
		'''
        if not s:
            return 0
        res = 0
        temp = 0
        for k in range(len(s)):
            if s[k] == ' ':
                if temp > 0:
                    # 处理最后一个为连续空格
                    res = temp
                temp = 0
            else:
                temp += 1
        if temp > 0:
            # 处理只有一个字符
            res = temp
        return res