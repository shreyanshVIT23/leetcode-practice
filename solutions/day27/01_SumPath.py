# Title: 112. Path Sum
# URL: https://leetcode.com/problems/path-sum/description/

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]
        curr = root
        while stack:
            [curr, total] = stack.pop()
            
            if curr.left is None and curr.right is None and total == targetSum:
                return True
            
            if curr.left:
                stack.append((curr.left, total + curr.left.val))
            if curr.right:
                stack.append((curr.right, total + curr.right.val))
            
        return False


def buildTreeFromArray(tree: List[int]) -> Optional[TreeNode]:
    if not tree or tree[0] is None:
        return None

    root = TreeNode(tree[0])
    queue = deque([root])
    i = 1

    while queue and i < len(tree):
        curr = queue.popleft()
        if i < len(tree) and tree[i] is not None:
            curr.left = TreeNode(tree[i])
            queue.append(curr.left)

        i += 1
        if i < len(tree) and tree[i] is not None:
            curr.right = TreeNode(tree[i])
            queue.append(curr.right)
        i += 1

    return root


null = None
sol = Solution()
print(sol.hasPathSum(buildTreeFromArray(
    [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]), 22))
