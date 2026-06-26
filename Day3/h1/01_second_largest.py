# - https://leetcode.com/problems/second-largest-digit-in-a-string/description/

class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1

        for x in s:
            if x.isdigit():
                x = int(x)

                if x > first:
                    second = first
                    first = x
                elif first > x > second:
                    second = x

        return second