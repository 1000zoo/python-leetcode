# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:

    """
    Runtime 224 ms Beats 16.77%
    """
    def solution1(self, s: str) -> int:
        l, r = 0, 0
        counter = {}
        answer = 0

        def add(alp):
            if alp not in counter.keys():
                counter[alp] = 0
            counter[alp] += 1
        def delete(alp):
            counter[alp] -= 1
            if counter[alp] == 0:
                del(counter[alp])

        while r <= len(s):
            if r < len(s):
                add(s[r])
            
            while l < r and len(counter.keys()) >= 3:
                answer += (len(s) - r)
                delete(s[l])
                l += 1
            r += 1
        
        return answer

    """
    Runtime 107 ms Beats 91.79%
    """
    def solution2(self, s: str) -> int:
        dp = [-1 for _ in range(3)]
        answer = 0

        for r in range(len(s)):
            dp[ord(s[r]) - ord('a')] = r
            answer += min(dp) + 1
        
        return answer