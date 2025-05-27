# Title: 111. Minimum Depth of Binary Tree
# URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        min_depth = 100000

        
        while stack:
            node, depth = stack.pop()
            
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)

            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
                
        return min_depth

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        queue = deque([root])
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return level