# Title: 507. Perfect Number
# URL: https://leetcode.com/problems/perfect-number/

import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0 if num == 1 else 1

        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                sum+=i
                if i!=num//i:
                    sum+=num//i
        
        return sum == num