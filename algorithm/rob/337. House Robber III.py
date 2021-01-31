

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        不能连续抢劫两家
        @param nums: 每一家的价值
        @return:
        """
        memo = {}
        return self.dp(root, memo)

    def dp(self, root, memo):
        if root is None:
            return 0
        if root in memo:
            return memo[root]

        # 抢劫，去下下家
        rob_now = root.val
        if root.left:
            rob_now += self.dp(root.left.left, memo) + self.dp(root.left.right, memo)
        if root.right:
            rob_now += self.dp(root.right.left, memo) + self.dp(root.right.right, memo)
        # 不抢，去下家
        rob_next = self.dp(root.left, memo) + self.dp(root.right, memo)
        # 选大的
        res = max(rob_now, rob_next)
        memo[root] = res
        return res
