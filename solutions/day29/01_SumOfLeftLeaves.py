# Title: 404. Sum of Left Leaves
# URL: https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 'c')]
        total = 0

        while stack:
            node, pos = stack.pop()
            if node.left is None and node.right is None and pos == 'l':
                total += node.val
            if node.left:
                stack.append((node.left, 'l'))
            if node.right:
                stack.append((node.right, 'r'))
        
        return total