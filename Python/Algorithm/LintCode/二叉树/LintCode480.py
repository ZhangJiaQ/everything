'''
480. Binary Tree Paths 

Given a binary tree, return all root-to-leaf paths.

深度优先+栈或队列
'''


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        res, stack = [], [(root, '')]
        if not root:
            return res
            
        while stack:
            node, text = stack.pop()
            if node:
                if not node.left and not node.right:
                    res.append(text+str(node.val))
                stack.append((node.left, text+str(node.val)+'->'))
                stack.append((node.right, text+str(node.val)+'->'))
                
        return res
