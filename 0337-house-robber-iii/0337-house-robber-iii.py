# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)

            leftrob, leftnot = dfs(node.left)
            rightrob, rightnot = dfs(node.right)

            robcurr = node.val + leftnot + rightnot

            skipcurr = (
                max(leftrob, leftnot)
                + max(rightrob, rightnot)
            )

            return (robcurr, skipcurr)

        return max(dfs(root))        