# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:

    """
    Runtime 35 ms Beats 40.48%
    """
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def helper(g):
            answer = 0
            gsum = 0
            i = 0

            for j in range(len(nums)):
                gsum += nums[j]
                while i <= j and gsum >= g:
                    answer += (len(nums) - j)
                    gsum -= nums[i]
                    i += 1
            return answer

        return helper(goal) - helper(goal + 1)