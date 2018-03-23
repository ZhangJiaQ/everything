'''
375. Clone Binary Tree 

For the given binary tree, return a deep copy of it.

'''


class Solution:
    """
    @param: root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if root:
            new_root = TreeNode(root.val)
        else:
            return None
        
        new_root.left = self.cloneTree(root.left)
        new_root.right = self.cloneTree(root.right)
        
        return new_root
        

