# Title: 150. Evaluate Reverse Polish Notation
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: int(a/b),
            "*": lambda a,b: a*b
        }
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                top = stack.pop()
                topPrev = stack.pop()
                stack.append(operations[token](topPrev, top))
        return stack.pop()