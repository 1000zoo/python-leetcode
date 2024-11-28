# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution:
    
    """
    Runtime 83 ms Beats 14.91%
    """
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        answer = 0
        flip = 0
        offset = [0] * len(nums)

        for i in range(len(nums)):
            flip += offset[i]
            nums[i] = nums[i] ^ 1 if flip % 2 == 1 else nums[i]

            if nums[i] == 0:
                if i + k > len(nums):
                    return -1
                if i + k < len(nums):
                    offset[i + k] -= 1

                answer += 1
                flip += 1
  
        return answer