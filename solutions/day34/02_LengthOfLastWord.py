# Title: 58. Length of Last Word
# URL: https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1
        
        if end < 0:
            return 0

        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        return end - start


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        start,end = 0,0
        for i in range(1,len(s)):
            if s[i] == " ":
                continue
            elif s[i-1] == " " and s[i] != " ":
                start = end = i
            elif s[i-1] != " " and s[i] != " ":
                end = i
        return end - start + 1