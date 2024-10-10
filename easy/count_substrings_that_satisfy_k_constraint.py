# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/

class Solution:

    """
    Runtime 272 ms Beats 6.42%
    """
    def solution1(self, s: str, k: int) -> int:
        answer = 0

        def isValid(s, k):
            cnt0 = 0
            cnt1 = 0

            for c in s:
                cnt0 += 1 if c == '0' else 0
                cnt1 += 1 if c == '1' else 0

            return cnt0 <= k or cnt1 <= k
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if isValid(s[i:j], k):
                    answer += 1
        
        return answer
