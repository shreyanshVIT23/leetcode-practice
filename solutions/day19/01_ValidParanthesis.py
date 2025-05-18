# Title: 20. Valid Paranthesis
# URL: https://leetcode.com/problems/valid-parentheses/description/

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack:
                    val = self.alternate(stack.pop())
                else:
                    return False
                if val != ch:
                    return False
        return True if not stack else False
    
    def alternate(self, char: chr) -> chr:
        if char == "(":
            return ")"
        elif char == "[":
            return "]"
        elif char == "{":
            return "}"