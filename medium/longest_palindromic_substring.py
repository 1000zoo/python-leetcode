# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:

    """
    Runtime 295 ms Beats 70.75%
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        def expandFromCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        answer = ""
        
        for i in range(len(s)):
            palindrome1 = expandFromCenter(i, i)
            palindrome2 = expandFromCenter(i, i + 1)
            
            if len(palindrome1) > len(answer):
                answer = palindrome1
            if len(palindrome2) > len(answer):
                answer = palindrome2
        
        return answer