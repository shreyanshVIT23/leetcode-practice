# Title: 1047. Remove All Adjacent Duplicates In String
# URL: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        ans = [s[0]]
        for i in range(1, len(s)):
            if ans and ans[-1] == s[i]:
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)