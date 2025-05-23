# Title: 169. Majority Element
# URL: https://leetcode.com/problems/majority-element/

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        max, maxVal = 0, 0 
        for k, v in count.items():
            if v > max:
                max = v
                maxVal = k
        
        return maxVal

