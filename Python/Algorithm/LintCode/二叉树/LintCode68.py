'''
68. Binary Tree Postorder Traversal 

Given a binary tree, return the postorder traversal of its nodes' values.
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here

        if not root:
            return []
        if root.left:
            self.postorderTraversal(root.left)
        
        if root.right:
            self.postorderTraversal(root.right)
            
        a.append(root.val)
            
        return a

