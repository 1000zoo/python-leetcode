class Solution(object):

    """
    Runtime 44 ms Beats 6.25%
    """
    def solution1(self, code, k):
        if k == 0:
            return [0 for _ in code]

        def next_index(i, length, sign):
            n = i + sign
            if n < 0:
                return length + n
            elif n >= length:
                return n - length
            else:
                return n
        answer = []
        sign = abs(k) // k
        length = len(code)

        for i in range(length):
            curr = i
            temp = 0
            for _ in range(abs(k)):
                curr = next_index(curr, length, sign)
                temp += code[curr]
            answer.append(temp)

        return answer

    