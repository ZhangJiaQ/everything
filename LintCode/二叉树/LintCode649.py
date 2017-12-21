'''
469. Identical Binary Tree

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.
'''


class Solution:
    """
    @param: a: the root of binary tree a.
    @param: b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # write your code here
        if a == None and b == None:
            return True
        
        if a and b and a.val == b.val:
            return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
        
        return False

]
