"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def recursive_solution(self, root):
        if not root:
            return True, 0
        # 递归调用左 右子树，左子树最下层节点height当然为0
        left_bool, left_height = self.recursive_solution(root.left)
        right_bool, right_height = self.recursive_solution(root.right)
        
        # 是否超限flag标志
        res_bool = False
        
        # 每次递归条件都判断是否超限
        # 一旦不符合则为False
        # 之后都不用再判断了，等递归调用结束后返回
        if left_bool and right_bool:
            if abs(left_height - right_height) < 2:
                res_bool = True
                
        
        return res_bool, max(left_height, right_height) + 1
    
    def isBalanced(self, root):
        # write your code here
        # 判断一个二叉树是不是平衡的
        return self.recursive_solution(root)[0]