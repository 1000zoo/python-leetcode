# https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/

class Solution:

    """
    Runtime 107 ms Beats 76.62%
    """
    def minimumLevels(self, possible: list[int]) -> int:
        possible = [-1 if p == 0 else p for p in possible]
        length = len(possible)

        alice = possible[0]
        bob = sum(possible[1:])

        for i in range(1, length):
            if alice > bob:
                return i
            alice += possible[i]
            bob -= possible[i]

        return -1

    """
    Runtime 211 ms Beats 34.41%
    """
    def minimumLevels(self, possible: list[int]) -> int:
        possible = [-1 if p == 0 else p for p in possible]
        possible.insert(0, 0)
        length = len(possible)
        for i in range(1, length):
            possible[i] += possible[i - 1]
        for i in range(1, length - 1):
            alice = possible[i] - possible[0]
            bob = possible[length - 1] - possible[i]
            if alice > bob:
                return i

        return -1
