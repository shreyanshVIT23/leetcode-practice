# Title: 114. Flatten Binary Tree to Linked List
# URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        Morris Method Takes 0(1) space
        """
        visit = root
        while visit is not None:
            if visit.left is not None:
                attach = visit.left
                while attach.right is not None:
                    attach = attach.right
                attach.right = visit.right
                visit.right = visit.left
                visit.left = None
            visit = visit.right

class Solution1:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            if prev:
                prev.right = node
                prev.left = None
            
            prev = node