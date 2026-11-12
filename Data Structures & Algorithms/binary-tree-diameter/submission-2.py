# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursion(self, node, node_height = None):
        if node_height is None:
            node_height = {}
        if not node.left and not node.right:
            node_height[node] = (0,0)
            return (0, node_height)
        elif not node.left and node.right:
            left, right, node_height = 0, *self.recursion(node.right)
            right += 1
            node_height[node] = (left, right)
            return (right, node_height)
        elif node.left and not node.right:
            left, node_height, right = *self.recursion(node.left), 0
            left += 1
            node_height[node] = (left, right)
            return (left, node_height)
        else:
            left, a, right, b = *self.recursion(node.left), *self.recursion(node.right)
            a.update(b)
            node_height = a
            left += 1
            right += 1
            node_height[node] = (left, right)
            return (max([left, right]), node_height)
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for every node, sum its left height and right height,
        # then take the max of every node.

        _, node_height = self.recursion(root)
        max_diameter = max(map(sum, node_height.values()))
        return max_diameter

        