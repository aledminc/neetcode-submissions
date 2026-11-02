# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # at every node, just switch its children from right to left
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            r, l = cur.right, cur.left
            if l:
                cur.right = l
                queue.append(cur.left)
            else:
                cur.right = l
            if r:
                cur.left = r
                queue.append(cur.left)
            else: 
                cur.left = r
        return root
            
