# Title: 66. Plus One
# URL: https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + carry
            carry = 0
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            if i == 0 and carry == 1 and digits[i] == 0:
                digits.insert(0, 1)
        return digits

sol = Solution()
print(sol.plusOne([1,2,3])) # [1,2,4]
print(sol.plusOne([4,3,2,1])) # [4,3,2,2]
print(sol.plusOne([9, 9])) # [1,0]