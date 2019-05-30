"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    73. 前序遍历和中序遍历树构造二叉树
    中文English
    根据前序遍历和中序遍历树构造二叉树.

    样例
    样例 1:

    输入：[],[]
    输出：{}
    解释：
    二叉树为空
    样例 2:

    输入：[2,1,3],[1,2,3]
    输出：{2,1,3}
    解释：
    二叉树如下
      2
     / \
    1   3
    注意事项
    你可以假设树中不存在相同数值的节点
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid_index = inorder.index(preorder[0])
        
        # 将前序数组分为左右子树 中序也分为左右两个子树
        root.left = self.buildTree(preorder[1:mid_index+1], inorder[:mid_index])
        root.right = self.buildTree(preorder[mid_index+1:], inorder[mid_index+1:])
        
        return root 