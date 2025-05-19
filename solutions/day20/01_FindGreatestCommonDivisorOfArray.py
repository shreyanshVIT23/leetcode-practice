# Title: 1979. Find Greatest Common Divisor of Array
# URL: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum, minNum = 0, 1001
        for val in nums:
            if val > maxNum:
                maxNum = val
            if val < minNum:
                minNum = val
        while minNum != 0:
            maxNum, minNum = minNum, maxNum % minNum
        return maxNum