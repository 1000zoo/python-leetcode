# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:

    """
    Runtime 40 ms Beats 30.98%
    """
    def countGoodSubstrings(self, s: str) -> int:
        def isGood(s):
            sset = set(list(s))
            return len(s) == len(sset)

        answer = 0

        for i in range(len(s) - 2):
            answer += 1 if isGood(s[i:i+3]) else 0

        return answer
