# Title: 34. Find First and Last Position of Element in Sorted Array
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

class Solution:
    from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(find_first):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if find_first:
                        right = mid - 1  
                    else:
                        left = mid + 1   
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        start = binary_search(find_first=True)
        end = binary_search(find_first=False)
        return [start, end]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        found = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if found == -1:
            return [-1, -1]

        left = right = found
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1

        return [left, right]