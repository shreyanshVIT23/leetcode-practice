# Title: 1249. Minimum Remove To Make Valid Paranthesis
# URL: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove.update(stack)
        return "".join(ch for i, ch in enumerate(s) if i not in to_remove)
