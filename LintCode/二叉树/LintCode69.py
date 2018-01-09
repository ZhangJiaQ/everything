'''
66. Binary Tree Preorder Traversal 

Given a binary tree, return the preorder traversal of its nodes' values.
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

global a
a = []
class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here

        if not root:
            return []
        a.append(root.val)
        
        if root.left:
            self.preorderTraversal(root.left)
        
        if root.right:
            self.preorderTraversal(root.right)
            
        
            
        return a
        return a

