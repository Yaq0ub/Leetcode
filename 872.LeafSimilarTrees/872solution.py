# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Define a helper function to perform a depth-first search
        def dfs(root: Optional[TreeNode], leaf: List[int]):
            # If the current node is None, return immediately
            if not root:
                return
            # If the current node is a leaf node, add its value to the leaf list
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            # Recursively call dfs on the left and right children
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        # Initialize two lists to store leaf sequences of both trees
        seq1, seq2 = [], []
        # Populate the leaf sequences by performing dfs on both trees
        dfs(root1, seq1)
        dfs(root2, seq2)
        # Compare the two leaf sequences and return True if they are identical, False otherwise
        return seq1 == seq2
