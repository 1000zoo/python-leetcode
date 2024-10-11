# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:

    """
    Runtime 470 ms Beats 34.59%
    """
    def longestSubarray(self, nums: list[int]) -> int:
        if sum(nums) == 0:
            return 0
        cnt0 = 0
        answer = 0
        l = 0

        for r in range(len(nums)):
            cnt0 += nums[r] ^ 1

            while cnt0 > 1:
                cnt0 -= nums[l] ^ 1
                l += 1

            answer = max(answer, r - l)
                    
        return answer if answer != 0 else len(nums) - 1