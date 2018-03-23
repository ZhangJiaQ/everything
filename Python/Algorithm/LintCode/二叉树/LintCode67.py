'''
67. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.
'''


global a
a = []


class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    
    def inorderTraversal(self, root):
        # write your code here

        if not root:
            return []
        if root.left:
            self.inorderTraversal(root.left)
        a.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
            
        return a
        
