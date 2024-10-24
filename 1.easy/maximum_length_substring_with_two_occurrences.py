# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution:

    """
    Runtime 7 ms Beats 97.44%
    """
    def maximumLengthSubstring(self, s: str) -> int:
        cnt_map = dict()
        answer = 0
        i = 0

        for j in range(len(s)):
            c = s[j]
            if c not in cnt_map.keys():
                cnt_map[c] = 0
            cnt_map[c] += 1
            while cnt_map[c] > 2:
                cnt_map[s[i]] -= 1
                i += 1
            answer = max(answer, j - i + 1)

        return answer