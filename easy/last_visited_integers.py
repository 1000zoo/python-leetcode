### https://leetcode.com/problems/last-visited-integers/

class Solution:
    """
    Runtime 41ms Beats 91.10
    B
    """
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        answer = []
        seen = []
        k = 0

        for num in nums:
            if num == -1:
                k += 1
                if k <= len(seen):
                    answer.append(seen[-k])
                else:
                    answer.append(-1)
            else:
                k = 0
                seen.append(num)
        
        return answer


