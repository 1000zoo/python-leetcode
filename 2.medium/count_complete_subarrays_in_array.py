# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:

    """
    Runtime 26 ms Beats 99.23%
    """
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        class HashMap:
            def __init__(self):
                self.m = dict()
            def add(self, num):
                if num not in self.m.keys():
                    self.m[num] = 0
                self.m[num] += 1
            def remove(self, num):
                if num not in self.m.keys():
                    return
                self.m[num] -= 1
                if self.m[num] == 0:
                    del(self.m[num])
            def size(self):
                return len(self.m.keys())

        answer = 0
        n = len(set(nums))
        i = 0
        hm = HashMap()

        for j in range(len(nums)):
            hm.add(nums[j])
            while i <= j and hm.size() == n:
                answer += (len(nums) - j)
                hm.remove(nums[i])
                i += 1

        return answer