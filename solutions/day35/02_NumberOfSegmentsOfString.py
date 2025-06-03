# Title: 434. Number of Segments in a String
# URL: https://leetcode.com/problems/number-of-segments-in-a-string/description/

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        for i in range(1, len(s)):
            if s[i] == " ":
                continue
            elif s[i-1] == " " and s[i] != " ":
                count += 1
        if s[0] != " ":
            count += 1  
        return count
