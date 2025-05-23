# Title: 32. Longest Valid Parentheses
# URL: https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                stack.pop()
                if stack:
                    length = max(length, idx - stack[-1])
                else:
                    stack.append(idx)
        return length
    
sol = Solution()
print(sol.longestValidParentheses("(()"))  # Output: 2