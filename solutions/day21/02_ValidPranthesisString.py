# Title: 678. Valid Parenthesis String
# URL: https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wildcard = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    if not wildcard:
                        print()
                        return False
                    k = wildcard.pop()
                    if i < k:
                        print(f"i:{i} k:{k} wildcard:{wildcard}")
                        return False
                else:
                    j = stack.pop()
            elif s[i] == "*":
                wildcard.append(i)    
        
        if stack:
            if len(stack) > len(wildcard):
                return False
            else:
                j = 0
                for i in range(len(stack)):
                    if stack[i] < wildcard[i]:
                        j+=1
                        continue
                    while stack[i] > wildcard[j]:
                        j+=1
                        if len(wildcard) == j:
                            return False
                    if len(stack)-i > len(wildcard)-j:
                        return False
        
        return True
