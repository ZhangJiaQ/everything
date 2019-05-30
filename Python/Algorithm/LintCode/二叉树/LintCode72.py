"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    72. 中序遍历和后序遍历树构造二叉树
        中文English
        根据中序遍历和后序遍历树构造二叉树

        样例
        样例 1:

        输入：[],[]
        输出：{}
        解释：
        二叉树为空
        样例 2:

        输入：[1,2,3],[1,3,2]
        输出：{2,1,3}
        解释：
        二叉树如下
          2
         / \
        1   3
        注意事项
        你可以假设树中不存在相同数值的节点
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if not inorder or not postorder:
            return None
            
        mid_index = inorder.index(postorder[-1])
        
        root = TreeNode(postorder[-1])
        
        # 分割中序遍历数组以及后序遍历数组
        
        root.left = self.buildTree(inorder[:mid_index], postorder[:mid_index]) 
        root.right = self.buildTree(inorder[mid_index+1:], postorder[mid_index:-1]) 
        
        return root
        