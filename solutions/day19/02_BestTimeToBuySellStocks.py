# Title:
# URL:

import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = math.inf
        minIdx = 0
        max = -math.inf
        maxIdx = -1

        for i in range(len(prices)):
            price = prices[i]
            if min > price and maxIdx < minIdx:
                min = price
                minIdx = i
            if price > min and price > max:
                max = price
                maxIdx = i
        return max - min if max>min else 0
        
sol = Solution()
print(sol.maxProfit([2,4,1]))  # Output: 2