# Title: 172. Factorial Trailing Zeroes
# URL: https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        count = 0
        i = 5
        while n // i > 0:
            count += n // i
            i *= 5
        return count

sol = Solution()
print(sol.trailingZeroes(0))  # Output: 1
print(sol.trailingZeroes(3))  