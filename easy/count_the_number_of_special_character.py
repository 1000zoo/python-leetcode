# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:

    """
    Runtime 33 ms Beats 80.02%
    """
    def numberOfSpecialChars(self, word: str) -> int:
        CONST = ord('a') - ord('A')
        alp_set = set(list(word))
        dup_set = set()

        for w in word:
            if ord('a') <= ord(w) <= ord('z'):
                s = chr(ord(w) - CONST)
                if s in alp_set:
                    dup_set.add(s)
            else:
                s = chr(ord(w) + CONST)
                if s in alp_set:
                    dup_set.add(s)

        return len(dup_set) // 2