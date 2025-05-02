# Title: 268. Missing Number
# URL: https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
        return None
