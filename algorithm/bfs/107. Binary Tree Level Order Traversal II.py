# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        help_stack = []
        if root:
            help_stack.append(root)
        while help_stack:
            temp = []
            new_help_stack = []
            for node in help_stack:
                temp.append(node.val)
                if node.left is not None:
                    new_help_stack.append(node.left)
                if node.right is not None:
                    new_help_stack.append(node.right)
            help_stack = new_help_stack
            result.insert(0, temp)
        return result
