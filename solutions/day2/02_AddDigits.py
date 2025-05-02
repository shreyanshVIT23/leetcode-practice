# Title: 258. Add Digits
# URL: https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num:
            digit = num%10
            num//=10
            sum+=digit
            if sum >= 10 and num == 0:
                num = sum
                sum = 0
        return sum
        