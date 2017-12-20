'''
97. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if root == None:
            return 0
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)

        return max(ldepth, rdepth) + 1