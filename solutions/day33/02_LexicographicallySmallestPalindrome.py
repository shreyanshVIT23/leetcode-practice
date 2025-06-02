# Title: 2697. Lexicographically Smallest Palindrome
# URL: https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right, n = 0, 0, len(s)
        if n%2 == 2:
            left, right = n//2 - 1, n//2 
        else:
            left, right = n//2 - 1, (n+1)//2
        
        while left >= 0 and right < n:
            char = chr(min(ord(s[right]) , ord(s[left])))
            if char == s[right] and char != s[left]:
                s = s[:left] + char + s[left+1:]
            elif char == s[left] and char != s[right]:
                s = s[:right] + char + s[right+1:]
            left -= 1
            right += 1
        return s

class Solution1:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s) 
        n = len(s)
        if n % 2 == 0:
            left, right = n // 2 - 1, n // 2
        else:
            left, right = n // 2 - 1, n // 2 + 1
        
        while left >= 0 and right < n:
            if s[left] != s[right]:
                s[left] = s[right] = min(s[left], s[right])
            left -= 1
            right += 1
        
        return ''.join(s)

class Solution2:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = []
        
        for a,b in zip(s[:n//2], s[n-1: (n-1)//2: -1]):
            if a > b:
                ans.append(b)
            else:
                ans.append(a)
        
        ans = ('').join(ans)
        if n%2 == 0:
            return ans + ans[::-1]
        else:
            return ans + s[n//2] + ans[::-1]

sol = Solution2()
print(sol.makeSmallestPalindrome("egcfz"))