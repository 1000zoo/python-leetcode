# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:

    """
    Runtime 75 ms Beats 93.59%
    """
    def longestOnes(self, nums: list[int], k: int) -> int:
        answer = 0
        cnt = 0
        i = 0

        for j in range(len(nums)):
            cnt += nums[j] ^ 1
            while cnt > k:
                cnt -= nums[i] ^ 1
                i += 1
            answer = max(answer, j - i + 1)

        return answer
