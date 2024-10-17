# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq

class Solution:

    """
    Runtime 467 ms Beats 7.23%
    """
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        cur_max = nums[0][0]

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])
        answer = [float('-inf'), float('inf')]

        while heap:
            cur_min, i, j = heapq.heappop(heap)
            if cur_max - cur_min < answer[1] - answer[0]:
                answer = [cur_min, cur_max]
            if j + 1 < len(nums[i]):
                heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
                cur_max = max(cur_max, nums[i][j + 1])
            else:
                break

        return answer
