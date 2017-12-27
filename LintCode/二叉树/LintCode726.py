'''
726. Check Full Binary Tree 

A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes. Conversely, there is no node in a full binary tree, which has one child node. More information about full binary trees can be found here.
'''


class Solution:
    """
    @param: : the given tree
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        # write your code here
        if not root:
            return False
        if not root.right and not root.left:
            return True 
        
        if not root.right or not root.left:
            return False
            
        left_bool = self.isFullTree(root.left)
        right_bool = self.isFullTree(root.right)
        
        if not left_bool or not right_bool:
            return False
            
        return True
