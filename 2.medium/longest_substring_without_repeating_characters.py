# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:

    """
    Runtime 44 ms Beats 95.08%
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        answer = 0
        dup = set()
        i, j = 0, 0

        while j < len(s):
            if s[j] not in dup:
                dup.add(s[j])
                j += 1
                continue
            answer = max(answer, j - i)
            while s[j] in dup:
                dup.remove(s[i])
                i += 1
            dup.add(s[j])
            j += 1

        return max(answer, j - i)

