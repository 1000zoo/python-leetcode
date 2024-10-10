# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:

    """
    Runtime 655 ms Beats 20.70%
    """
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def mostK(nums, k):
            l, r = 0, 0
            answer = 0
            count = 0

            for r in range(len(nums)):
                count += nums[r] % 2

                while count > k:
                    count -= nums[l] % 2
                    l += 1
                answer += (r - l + 1)

            return answer

        return mostK(nums, k) - mostK(nums, k - 1)
