# Title: 129. Sum Root to Leaf Numbers
# URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: 'TreeNode') -> int:
        total = 0
        stack = [(root, root.val)]
        while stack:
            node, rootToLeaf = stack.pop()
            if not node.left and not node.right:
                total += rootToLeaf
            if node.left:
                stack.append((node.left, rootToLeaf*10 + node.left.val))
            if node.right:
                stack.append((node.right, rootToLeaf*10 + node.right.val))
        return total