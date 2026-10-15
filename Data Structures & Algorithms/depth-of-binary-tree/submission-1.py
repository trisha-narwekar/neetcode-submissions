# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # method(node)
        def dfs(node):
            # base case - node null
            if not node:
                return 0
            else:
                # left depth - dfs(node.left)
                leftDepth = dfs(node.left)
                # right depth - dfs(node.right)
                rightDepth = dfs(node.right)
                # return 1 + max(left, right)
                return 1 + max(leftDepth, rightDepth)
        return dfs(root)