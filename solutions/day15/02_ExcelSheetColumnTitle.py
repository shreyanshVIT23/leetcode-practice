# Title: 168. Excel Sheet Column Title
# URL: https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ch = ""
        while columnNumber:
            columnNumber-=1
            ch = chr(( columnNumber % 26 ) + ord('A')) + ch
            columnNumber//=26
        return ch
