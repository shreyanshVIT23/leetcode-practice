# Title: Minimum Domino Rotations For Equal Row
# URL: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


from typing import Counter, List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counts = Counter(tops+bottoms)
        most_common = counts.most_common(1)[0][0]
        [tops, bottoms] = [bottoms, tops] if tops.count(
            most_common) < bottoms.count(most_common) else [tops, bottoms]
        conversions = 0
        for i in range(len(tops)):
            if tops[i] == most_common or bottoms[i] == most_common:
                if tops[i] != most_common:
                    tops[i], bottoms[i] = bottoms[i], tops[i]
                    conversions += 1
            else:
                return -1
        return len(tops) - conversions if conversions > len(tops) - conversions else conversions


sol = Solution()
tops = [1, 2, 1, 1, 1, 2, 2, 2]
bottoms = [2, 1, 2, 2, 2, 2, 2, 2]
result = sol.minDominoRotations(tops, bottoms)
print(result)  # Output: 2
