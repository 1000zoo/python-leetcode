# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:

    """
    Runtime 64 ms Beats 92.22 %
    """
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = min(brackets[0][0], income) * brackets[0][1] / 100
        if brackets[0][0] >= income:
            return tax

        for i in range(1, len(brackets)):
            b0 = brackets[i - 1]
            b1 = brackets[i]

            if b1[0] >= income:
                tax += (income - b0[0]) * b1[1] / 100
                break
            tax += (b1[0] - b0[0]) * b1[1] / 100


        return tax
        