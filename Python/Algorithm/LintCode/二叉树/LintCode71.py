"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    71. 二叉树的锯齿形层次遍历
    中文English
    给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行） 

    样例
    样例 1:

    输入:{1,2,3}
    输出:[[1],[3,2]]
    解释:
        1
       / \
      2   3
    它将被序列化为 {1,2,3}
    样例 2:

    输入:{3,9,20,#,#,15,7}
    输出:[[3],[20,9],[15,7]]
    解释:
        3
       / \
      9  20
        /  \
       15   7
    它将被序列化为 {3,9,20,#,#,15,7}
    
    """
    
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        # 创建结果数组
        result = []
        # 创建node数组
        nodes = []
        nodes.append(root)
        # 1 左遍历 -1 右遍历
        flag = 1
        while nodes:
            temp = []
            len_num = len(nodes)
            # 层次遍历+左右顺序变换
            for _ in range(len_num):
                node = nodes.pop(0)
                temp.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if flag == -1:
                temp = temp[::-1]
            result.append(temp)
            flag *= -1
        return result 
            