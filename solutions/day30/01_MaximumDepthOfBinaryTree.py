# Title: 104. Maximum Depth of Binary Tree
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        depth = 0
        if not root:
            return 0
            
        while stack:
            node, level = stack.pop()
            depth = max(depth, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return depth

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1