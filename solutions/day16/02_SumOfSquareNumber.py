# Title: 633. Sum of Square Numbers
# URL: https://leetcode.com/problems/sum-of-square-numbers/description/
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c)+1)
        while a <= b:
            if a**2 + b**2 == c:
                return True
            elif a**2 + b**2 > c:
                b-=1
            elif a**2 + b**2 < c:
                a+=1
        return False

sol = Solution()
print(sol.judgeSquareSum(16))  # Output: True