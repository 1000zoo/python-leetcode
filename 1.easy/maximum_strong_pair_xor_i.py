# https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution:

    """
    Runtime 116 ms Beats 41.33%
    """
    def solution1(self, nums: list[int]) -> int:
        def isStrongPair(x, y):
            return abs(x - y) <= min(x, y)
        
        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if isStrongPair(nums[i], nums[j]):
                    answer = max(answer, nums[i] ^ nums[j])
        
        return answer