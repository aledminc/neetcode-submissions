# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurs(self, node, count):
        depths = []
        if not node.left and not node.right:
            return count
        if node.left:
            depths.append(self.recurs(node.left, count + 1))
        if node.right:
            depths.append(self.recurs(node.right, count + 1))
        return max(depths)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.recurs(root, 1)