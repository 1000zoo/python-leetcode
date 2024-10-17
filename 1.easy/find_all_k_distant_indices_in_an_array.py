# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:

    """
    Runtime 188 ms Beats 49.78%
    """
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        key_indices = [i for i, n in enumerate(nums) if n == key]
        answer = []
        for index in key_indices:
            answer.extend(list(range(max(0, index - k), min(len(nums), index + k + 1))))
        s = set(answer)
        return sorted(list(s))