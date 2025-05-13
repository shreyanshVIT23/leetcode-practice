# Title: 1822. Sign of the Product of an Array
# URL: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negCount = 0
        for num in nums:
            if self.signFunc(num) == -1:
                negCount += 1
            elif self.signFunc(num) == 0:
                return 0
        return -1 if negCount % 2 else 1

    def signFunc(self, x: int) -> int:
        return 1 if x > 0 else (
            -1 if x < 0 else 0
        )
