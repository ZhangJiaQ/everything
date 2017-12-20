'''
175. Invert Binary Tree

Invert a binary tree.

'''


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return None

        if root.left or root.right:
            root.left, root.right = root.right, root.left

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root
