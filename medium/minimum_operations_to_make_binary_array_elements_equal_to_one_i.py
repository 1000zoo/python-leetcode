# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution:

    """
    Runtime 1004 ms Beats 76.41%
    """
    def minOperations(self, nums: list[int]) -> int:
        answer = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                answer += 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1

        return answer if nums[-1] == nums[-2] == 1 else -1