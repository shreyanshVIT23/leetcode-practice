# Title: 94. Binary Tree Inorder Traversal
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        tree = []
        head = root
        while head or stack:
            while head:
                stack.append(head)
                head = head.left
            head = stack.pop()
            tree.append(head.val)
            head = head.right
        return tree

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        binaryTree = []
        self.traversal(root, binaryTree)
        return binaryTree
    
    def traversal(self, root: Optional[TreeNode], tree: List[int]) -> None:
        if root:
            self.traversal(root.left, tree)
            tree.append(root.val)
            self.traversal(root.right, tree)