# Title: 189. Rotate Array
# URL: https://leetcode.com/problems/rotate-array/description/

from typing import List
import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        i,j = 0, k-1
        while i<j:
            nums[i], nums[j] = nums[j] , nums[i]
            i+=1
            j-=1
        i, j = k, len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j] , nums[i]
            i+=1
            j-=1
        print(nums)
    
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        curr, prev = 0, nums[0]
        cycles = math.gcd(n, k)
        while cycles < 3*n:
            curr = (curr + k) % n
            temp = nums[curr]
            nums[curr] = prev
            prev = temp
            cycles+=3

sol = Solution1()
sol.rotate([1,2,3,4,5,6,7], 3)