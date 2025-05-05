# Title: 202. Happy Number
# URL: https://leetcode.com/problems/happy-number/description/

import math


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        while n > 1:
            sum = 0
            while n != 0:
                sum += int(math.pow((n % 10), 2))
                n //= 10
            n = sum
            if n in nums:
                return False
            else:
                nums.append(n)
        return True if n == 1 else False


sol = Solution()
print(sol.isHappy(2))  # Output: True
