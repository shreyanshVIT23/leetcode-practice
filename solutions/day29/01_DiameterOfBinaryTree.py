# Title: 543. Diameter of Binary Tree
# URL: https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def buildTreeFromArray(tree: List[int]):
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        node_height = {}
        diameter = 0
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                left = node_height.get(node.left, 0)
                right = node_height.get(node.right, 0)
                node_height[node] = max(left+1, right+1)
                diameter = max(diameter, left+right)
        return diameter

class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxdepth: int = 0
        
        def find_dpth(node: TreeNode|None) -> int:
            if node is None:
                return 0
            nonlocal maxdepth
            left = find_dpth(node.left)
            right = find_dpth(node.right)
            maxdepth = max(maxdepth, left+right)
            return 1 + max(left, right)
        
        find_dpth(root)
        return maxdepth
            
        
sol = Solution()
print(sol.diameterOfBinaryTree((TreeNode.buildTreeFromArray([1,2,3,4,5]))))