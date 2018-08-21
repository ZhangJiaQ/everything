class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
		'''
		423. 有效的括号序列
		给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

		样例
		括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。
		'''
        brackets_dict = {'{': '}', '[': ']', '(': ')'}
        temp = []
        for t in s:
            if t in ('{', '[', '('):
                temp.append(t)
            else:
                if temp:
                    temp_str = brackets_dict.get(temp.pop(), '')
                    if temp_str !=  t:
                        return False
                else:
                    return False
        if temp:
            return False
        return True