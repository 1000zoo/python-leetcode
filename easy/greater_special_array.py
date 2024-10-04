class Solution:

    """
    Runtime 44 ms Beats 29.09%
    """
    def solution1(self, nums: list[int]) -> int:
        for x in range(1, len(nums) + 1):
            cnt = 0
            for num in nums:
                if x <= num:
                    cnt += 1
            if x == cnt:
                return x
        return -1

    """
    Runtime 32 ms Beats 92.41%
    """
    def solution2(self, nums: list[int]) -> int:
        nums.sort()
        index = 0
        
        for x in range(len(nums) + 1):
            while index < len(nums) and nums[index] < x:
                index += 1
            if len(nums) - index == x:
                return x

        return -1
        