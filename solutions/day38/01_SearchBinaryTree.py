# Title: 700. Search in a Binary Search Tree
# URL: https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: 'TreeNode', val: int) -> 'TreeNode':
        curr = root
        while curr:
            if curr.val == val:
                break
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return curr