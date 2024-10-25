# https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:

    """
    Runtime 162 ms Beats 90.16%
    """
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def helper(k):
            answer = 0
            counter = dict()
            i = 0

            for j in range(len(nums)):
                if not nums[j] in counter.keys():
                    counter[nums[j]] = 0
                counter[nums[j]] += 1
                
                while i <= j and len(counter.keys()) == k:
                    answer += (len(nums) - j)
                    counter[nums[i]] -= 1
                    if counter[nums[i]] == 0:
                        del(counter[nums[i]])                        
                    i += 1

            return answer

        return helper(k) - helper(k + 1)

