# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:

    """
    Runtime 47 ms Beats 36.04%
    """
    def bruteforce(self, colors: list[int]) -> int:
        max_length = 0

        for i in range(len(colors) - 1):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    max_length = max(max_length, j - i)
        
        return max_length
    

    """
    Runtime 36 ms Beats 88.12%
    """
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        i, j = 0, n - 1

        while colors[0] == colors[j]:
            j -= 1
        while colors[-1] == colors[i]:
            i += 1
        return max(n - i - 1, j)