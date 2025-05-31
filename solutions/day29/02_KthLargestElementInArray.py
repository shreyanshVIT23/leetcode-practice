# Title: 215. Kth Largest Element in an Array
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot_i = random.randint(left, right)
            nums[pivot_i], nums[right] = nums[right], nums[pivot_i]
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] > pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i+=1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        left, right = 0, len(nums) - 1
        k = k - 1
        while left <= right:
            idx = partition(left, right) 
            if idx > k:
                right = idx - 1
            elif idx < k:
                left = idx + 1
            else:
                return nums[idx]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        return heapq.heappop(min_heap)