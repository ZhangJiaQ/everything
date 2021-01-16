# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        left_status = True
        right_status = True
        if root:
            if root.left:
                left_status = self.dfs(root.left, root.val, 'left')
            if root.right:
                right_status = self.dfs(root.right, root.val, 'right')
        return left_status and right_status

    def dfs(root, father_node_val, _type):
        pass

