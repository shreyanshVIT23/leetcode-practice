# Title: 224. Basic Calculator
# URL: https://leetcode.com/problems/basic-calculator/

import math
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        values = []
        operators = []
        i = 0
        s = s.replace(" ", "")
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i+=1
                values.append(num)
            elif s[i] == "(":
                operators.append(s[i])
                i+=1
            elif s[i] == ")":
                while operators[-1] != "(":
                    self.evaluate(operators, values)
                operators.pop()
                i+=1
            elif s[i] in "+-*/":
                if s[i] == '-' and (i == 0 or s[i - 1] in "(+-*/"):
                    values.append(0)
                while (operators and operators[-1] != "("
                and self.priority(operators[-1]) >= self.priority(s[i])):
                    self.evaluate(operators, values)
                operators.append(s[i])
                i+=1
        while operators:
            self.evaluate(operators, values)
        return values[0]     


    def priority(self, ch: str) -> int:
        if ch in  "+-":
            return 1
        elif ch in "*/":
            return 2
        elif ch in  "()":
            return 3
        return 0
    
    def evaluate(self, operators: List[str], values: List[int]):
        right = values.pop()
        left = values.pop()
        op = operators.pop()

        if op == "+":
            values.append( left + right)
        elif op == "-":
            values.append(left - right)
        elif op == "*":
            values.append(left * right)
        elif op == "/":
            values.append(math.trunc(left / right))

sol = Solution()
print(sol.calculate("1-(     -2)"))  # Output: 7
