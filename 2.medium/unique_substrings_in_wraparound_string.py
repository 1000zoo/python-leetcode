# https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution:

    """
    Runtime 49 ms Beats 63.41%
    """
    def findSubstringInWraproundString(self, s: str) -> int:
        A = ord('a')
        
        dp = [0 for _ in range(26)]
        answer = 1
        prev = 1
        dp[ord(s[0]) - A] = 1

        for i in range(1, len(s)):
            if (ord(s[i-1]) - A + 1) % 26 == ord(s[i]) - A:
                prev += 1
            else:
                prev = 1
            if dp[ord(s[i]) - A] < prev:
                answer += prev - dp[ord(s[i]) - A]
                dp[ord(s[i]) - A] = prev

        return answer