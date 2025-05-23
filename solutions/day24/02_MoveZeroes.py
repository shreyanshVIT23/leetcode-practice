# Title: 283. Move Zeroes
# URL: https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i <= len(nums):
            if nums[i] == 0:
                idx = i
                while i < len(nums) and nums[i] == 0:
                    i+=1
                if i == len(nums):
                    break
                nums[idx] , nums[i] = nums[i], nums[idx]
                i = idx
            else:
                i+=1
        print(nums)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


sol = Solution()
sol.moveZeroes([0,1,0,3,12])