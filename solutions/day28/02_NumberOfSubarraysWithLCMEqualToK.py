# Title: 2470. Number of Subarrays With LCM Equal to K
# URL: https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/

from typing import List
from math import lcm


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        result = 0

        for i in range(len(nums)):
            val = nums[i]
            if val == k:
                result += 1
            for j in range(i+1, len(nums)):
                val = lcm(val, nums[j])
                if val == k:
                    result += 1
                elif val > k:
                    break

        return result
