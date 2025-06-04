# Title: 345. Reverse Vowels of a String
# URL: https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        first, last = 0, len(s)-1
        s = list(s)
        while first < last:
            if s[first].lower() not in "aeiou":
                first+=1
            if s[last].lower() not in "aeiou":
                last -= 1
            if s[first].lower() in "aeiou" and s[last].lower() in "aeiou":
                s[first], s[last] = s[last], s[first]
                first += 1
                last -= 1
        return "".join(s)
