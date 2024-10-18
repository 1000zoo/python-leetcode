# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:

    """
    Runtime 127 ms Beats 100.00%
    """
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        answer = 0
        i = -1
        minI, maxI = -1, -1

        for j in range(len(nums)):
            num = nums[j]
            if not (minK <= num <= maxK):
                i, minI, maxI = j, j, j
            minI = j if num == minK else minI
            maxI = j if num == maxK else maxI
            answer += min(minI, maxI) - i

        return answer
