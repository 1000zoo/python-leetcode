# https://leetcode.com/problems/alternating-groups-i/

class Solution:

    """
    Runtime 52 ms Beats 54.59%
    """
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        answer = 0
        
        for i in range(len(colors)):
            c1 = colors[i]
            c2 = colors[(i + 1) % len(colors)]
            c3 = colors[(i + 2) % len(colors)]
            if c1 == c3 and c1 != c2:
                answer += 1

        return answer