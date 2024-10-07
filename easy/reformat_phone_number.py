# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    
    """
    Runtime 35 ms Beats 51.97
    """
    def reformatNumber(self, number: str) -> str:
        digits = []
        for n in number:
            if n == ' ' or n == '-':
                continue
            digits.append(n)
        answer = []
        while len(digits) > 4:
            temp = ""
            for _ in range(3):
                temp += digits.pop(0)
            answer.append(temp)

        if len(digits) < 4:
            answer.append("".join(digits))
        else:
            answer.append("".join(digits[:2]))
            answer.append("".join(digits[2:]))

        return "-".join(answer)