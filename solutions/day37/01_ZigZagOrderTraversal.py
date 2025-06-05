# Title: 103. Binary Tree Zigzag Level Order Traversal
# URL:

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def buildTreeFromArray(tree: List[int]) -> 'TreeNode':
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

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root, 0])
        ans = [[]]
        while queue:
            node, level = queue.popleft()
            if len(ans) <= level:
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        switch = 1
        for i in range(len(ans)):
            if switch:
                ans[i].reverse()
            switch = switch ^ 1
        return ans


null = None
sol = Solution()
print(sol.zigzagLevelOrder(
    TreeNode.buildTreeFromArray([1, 2, 3, 4, null, null, 5])))
