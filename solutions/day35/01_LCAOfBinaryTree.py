# Title: 236. Lowest Common Ancestor of a Binary Tree
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, [root])]
        parent_p, parent_q = [], []
        while stack:
            node, parentTree = stack.pop()
            if node == p:
                parent_p = parentTree
            if node == q:
                parent_q = parentTree
            if parent_p != [] and parent_q != []:
                break
            if node.left:
                stack.append((node.left, parentTree + [node.left]))
            if node.right:
                stack.append((node.right, parentTree + [node.right]))
        parent_q = set(parent_q)
        for i in reversed(parent_p):
            if i in parent_q:
                return i
        return None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        if not p and not q:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root