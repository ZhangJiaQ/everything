'''
69. Binary Tree Level Order Traversal 

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        
        if not root:
            return res
            
        q = [root]
        
        while q:
            res.append([x.val for x in q])
            
            new_q = []
            for x in q:
                if x.left:
                    new_q.append(x.left)
                if x.right:
                    new_q.append(x.right)
                    
            q = new_q
        
        return res
