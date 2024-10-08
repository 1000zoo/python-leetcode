# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution:

    """
    Runtime 61 ms Beats 37.03%
    """
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        answer = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                answer += 1 if self.isPrefixAndSuffix(words[i], words[j]) else 0
        return answer

    def isPrefixAndSuffix(self, w1: str, w2: str) -> bool:
        return w1 == w2[:len(w1)] and w1 == w2[-len(w1):]