# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

from collections import defaultdict

class Solution:

    """
    Runtime 119 ms Beats 51.90%
    """
    def minSteps(self, s: str, t: str) -> int:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        answer = 0

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        for key in s_dict:
            c1, c2 = s_dict[key], t_dict[key]
            if c1 > c2:
                answer += (c1 - c2)
        return answer