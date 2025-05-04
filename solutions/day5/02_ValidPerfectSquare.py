# Title: 367. Valid Pefect Square
# URL: https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i**2 <= num:
            if i**2 == num:
                return True
            i += 1
        return False
