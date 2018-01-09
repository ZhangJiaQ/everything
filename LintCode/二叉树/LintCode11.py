'''
11. Search Range in Binary Search Tree 

Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.
'''
global res
res = []

class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return res
        while root.right and k1 > root.val:
            root = root.right
        while root.left and k2 < root.val:
            root = root.left
        
        self.searchRange(root.left, k1, k2)
        
        if root.val >= k1 and root.val <= k2:
            res.append(root.val)
        
        self.searchRange(root.right, k1, k2)

        return res
        
