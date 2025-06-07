# Title: 125. Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s)-1
        while first < last:
            while not s[first].isalnum() and first < last:
                first+=1
            while not s[last].isalnum() and first < last:
                last-=1
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True