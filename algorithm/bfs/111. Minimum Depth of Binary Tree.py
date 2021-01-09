# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        result = 0

        help_stack = []
        if root:
            help_stack.append(root)

        while len(help_stack) > 0:
            result += 1
            new_help_stack = []
            for node in help_stack:
                if node.left:
                    new_help_stack.append(node.left)
                if node.right:
                    new_help_stack.append(node.right)
                if node.left is None and node.right is None:
                    return result
            help_stack = new_help_stack

        return result
