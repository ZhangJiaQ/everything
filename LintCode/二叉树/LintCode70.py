'''
70. Binary Tree Level Order Traversal II 

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
'''


class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        res = []
        if not root:
            return res
            
        q = [root]
        
        while q:
            temp = []
            res.append([x.val for x in q])
            for x in q:
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            
            q = temp
        res = res[::-1]
        return res
        return True
