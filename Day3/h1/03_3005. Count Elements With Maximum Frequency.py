# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/


from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx = max(freq.values())
        return sum(v for v in freq.values() if v == mx)