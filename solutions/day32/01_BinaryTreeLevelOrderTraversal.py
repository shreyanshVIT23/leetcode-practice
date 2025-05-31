# Title: 102. Binary Tree Level Order Traversal
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        binaryTree = [[root.val]]
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
                if level+1 >= len(binaryTree):
                    binaryTree.append([node.left.val])
                else:
                    binaryTree[level+1].append(node.left.val)
            if node.right:
                queue.append((node.right, level + 1))
                if level + 1 >= len(binaryTree):
                    binaryTree.append([node.right.val])
                else:
                    binaryTree[level+1].append(node.right.val)
        return binaryTree
