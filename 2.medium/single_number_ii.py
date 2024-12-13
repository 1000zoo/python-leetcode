# https://leetcode.com/problems/single-number-ii/

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        table = defaultdict(int)
        for num in nums:
            table[num] += 1
        table = dict(table)
        for key in table:
            if table[key] != 3:
                return key
        return -1
        