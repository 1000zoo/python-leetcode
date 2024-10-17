# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:

    """
    Runtime 33 ms Beats 75.85%
    """
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0

        for i, alp in enumerate(columnTitle):
            a = (ord(alp) - ord('A') + 1)
            digits = pow(26, len(columnTitle) - i - 1)
            answer += a * digits

        return answer
