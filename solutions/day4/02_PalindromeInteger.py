# Title: Palindrome Number
# URL: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x

sol = Solution()
x = 121
result = sol.isPalindrome(x)
print(result)  # Output: True