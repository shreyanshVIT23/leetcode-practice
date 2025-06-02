# Title: 199. Binary Tree Right Side View
# URL: https://leetcode.com/problems/binary-tree-right-side-view/


from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = [root.val]
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node.right:
                queue.append((node.right,level+1))
                if len(result) <= level+1:
                    result.append(node.right.val)
            if node.left:
                queue.append((node.left, level+1))
                if len(result) <= level+1:
                    result.append(node.left.val)
        return result