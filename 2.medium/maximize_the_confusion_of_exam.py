# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    
    """
    Runtime 242 ms Beats 78.77%
    """
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxLength(c):
            answer = 0
            cnt = 0
            i = 0
            for j in range(len(answerKey)):
                cnt += 1 if answerKey[j] != c else 0
                if cnt > k:
                    while answerKey[i] == c:
                        i += 1
                    i += 1
                    cnt -= 1
                answer = max(answer, j - i + 1)
            return answer
                
        return max(maxLength('T'), maxLength('F'))
