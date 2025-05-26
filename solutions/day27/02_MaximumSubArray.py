# Title: 53. Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/description/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        i = 0
        for val in nums:
            if val < (val + dp[i]):
                dp[i+1] = val + dp[i]
            else:
                dp[i+1] = val
            i+=1
        return max(dp)

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            total = max(nums[i], nums[i] + total)
            if total > max_sum:
                max_sum = total
        return max_sum

sol = Solution2()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
