# Title: 2108. Find First Palindromic String in the Array
# URL: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

class Solution:
    def firstPalindrome(self, words: 'list[str]') -> 'str':
        for word in words:
            if word == word[::-1]:
                return word

        return ""