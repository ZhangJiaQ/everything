__author__ = 'Judge'
'''LintCode 569.
569. ��λ��� 
����һ���Ǹ����� num�������Ľ�����λ�ϵ�������ӣ�ֱ���õ�һ��һλ��������
'''
class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        while num // 10 > 0:
            num = num // 10 + num % 10

        return num