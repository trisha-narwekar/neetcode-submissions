# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(node):
            # base case 1 - root is null/reached the end
            if not node:
                return 0
            # calculate max of left and right, recursive
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            return 1 + max(leftDepth, rightDepth)
        return dfs(root)