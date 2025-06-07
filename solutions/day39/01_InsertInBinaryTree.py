# Title: 701. Insert into a Binary Search Tree
# URL: https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: "int" = val
        self.left: 'TreeNode|None' = left
        self.right: 'TreeNode|None' = right
        
class Solution:
    def insertIntoBST(self, root: 'TreeNode|None', val: int) -> 'TreeNode':
        if not root:
            return TreeNode(val)
        curr = root
        prev = None
        while curr:
            prev = curr
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right
        if prev.val > val:
            prev.left = TreeNode(val)
        elif prev.val < val:
            prev.right = TreeNode(val)
        return root
            
