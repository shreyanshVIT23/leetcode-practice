# Title: 119. Pascal's Triangle II
# URL: https://leetcode.com/problems/pascals-triangle-ii/description/

import math
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array = [0 for _ in range(rowIndex+1)]
        for i in range(rowIndex+1):
            array[i] = math.comb(rowIndex, i)        
        return array