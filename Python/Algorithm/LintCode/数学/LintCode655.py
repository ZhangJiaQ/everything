__author__ = 'Judge'
'''LintCode 655.
655. Big Integer Addition 
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
'''
'''
add in repeate part
'''
class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
         # write your code here
        
        result = ''
        
        len_cha = len(num1)-len(num2) if len(num1)>len(num2) else len(num2)-len(num1)
        
        for i in range(len_cha):
            if len(num1) > len(num2):
                num2 = '0' + num2
            if len(num2) > len(num1):
                num1 = '0' + num1
        
        
        
        flag = 0
        
        for i in range(1,len(num1)+1):
            
            if flag == 1:
                res = int(num1[-i]) + int(num2[-i]) + 1
            else:
                res = int(num1[-i]) + int(num2[-i])
                
            flag = 0
            
            if res >= 10:
                flag = 1
                res %= 10
            result += str(res)
            
        if flag == 1:
            result = result + '1' 
        
        result = result[::-1]
        
        
        return result
