# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:

    """
    Runtime 119 ms Beats 99.60%
    """
    def minSwaps(self, nums: list[int]) -> int:
        count0 = [0 for _ in nums]
        size = sum(nums)
        count0[0] = size - sum(nums[:size])

        for i in range(1, len(nums)):
            count0[i] = count0[i - 1]
            if nums[i - 1] == 0:
                count0[i] -= 1
            if nums[(i + size - 1) % len(nums)] == 0:
                count0[i] += 1

        return min(count0)
        