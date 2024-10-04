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
        
    """
    Runtime 32 ms Beats 92.41%
    """
    def specialArray(self, nums: list[int]) -> int:
        length = len(nums)
        freq = [0 for n in range(length + 1)]

        for i in range(length):
            freq[min(length, nums[i])] += 1
        
        prefix = 0
        for i in range(length, 0, -1):
            prefix += freq[i]
            if i == prefix:
                return i
        
        return -1