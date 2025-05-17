# Title: 217. Contains Duplicate
# URL: https://leetcode.com/problems/contains-duplicate/description/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for val in nums:
            if val in hashMap:
                return True
            else:
                hashMap[val] = 1
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)