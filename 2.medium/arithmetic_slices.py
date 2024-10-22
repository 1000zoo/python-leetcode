# https://leetcode.com/problems/arithmetic-slices/

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        
        answer, i = 0, 0
        d = nums[1] - nums[0]
    
        for j in range(1, len(nums) - 1):
            curr_d = nums[j + 1] - nums[j] 
            if d != curr_d:
                d = curr_d
                i = j
                continue
            answer += j - i

        return answer