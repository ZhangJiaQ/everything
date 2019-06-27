class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        """
        29. Interleaving String
        中文English
        Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

        Example
        Example 1:

        Input:
        "aabcc"
        "dbbca"
        "aadbbcbcac"
        Output:
        true
        Example 2:

        Input:
        ""
        ""
        "1"
        Output:
        false
        Example 3:

        Input:
        "aabcc"
        "dbbca"
        "aadbbbaccc"
        Output:
        false
        Challenge
        O(n2) time or better


        动态规划
        设置一个二维数组 用于记录数组s1子串是否正确
        并且也用于记录数组s2子串是否正确
        之后循环n^2次数计算两个子串上一位是否均等 并且数组元素上一位为True
        记录成功后求出二维数组末尾是否为True
        """
        if len(s1) + len(s2) != len(s3):
            return False
            
        dynamic_planning = [[False for i in range(len(s1) + 1)] for k in range(len(s2) + 1)]
        
        dynamic_planning[0][0] = True 
        
        for index, value in enumerate(s1, start = 1):
            dynamic_planning[0][index] = dynamic_planning[0][index - 1] and value == s3[index-1] 
        
        for index, value in enumerate(s2, start = 1):
            dynamic_planning[index][0] = dynamic_planning[index - 1][0] and value == s3[index-1] 
        
        for index1 in range(1, len(s1)+1):
            for index2 in range(1, len(s2)+1):
                dynamic_planning[index2][index1] = (dynamic_planning[index2 - 1][index1] and s2[index2 - 1] == s3[index2+index1-1]) or (dynamic_planning[index2][index1 - 1] and s1[index1 - 1] == s3[index2+index1-1])
                
        return dynamic_planning[len(s2)][len(s1)]