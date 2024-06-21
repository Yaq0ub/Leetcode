# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is None, the depth is 0
        if not root:
            return 0
        
        # Recursively find the depth of the left subtree and the right subtree,
        # then take the maximum of both and add 1 to include the current node.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
