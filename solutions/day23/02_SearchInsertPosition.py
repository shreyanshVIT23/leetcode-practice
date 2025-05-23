# Title: 35. Search Insert Position
# URL: https://leetcode.com/problems/search-insert-position/description/

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = 0
        prevMid = -1
        
        while mid != prevMid: 
            prevMid = mid
            mid = low+(high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid
        return high if nums[high] >= target else high+1

sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))  # Output: 2
print(sol.searchInsert([1,3,5,6], 2))  # Output: 1
print(sol.searchInsert([1,3,5,6], 7))  # Output: 4
print(sol.searchInsert([1,3,5,6], 0))  # Output: 0
print(sol.searchInsert([1, 3], 1))  # Output: 0