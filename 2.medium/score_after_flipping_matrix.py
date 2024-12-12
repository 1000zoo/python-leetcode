# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:

    """
    Runtime 3 ms Beats 20.61%
    """
    def matrixScore(self, grid: list[list[int]]) -> int:
        def flipRow(row):
            for i in range(len(grid[0])):
                grid[row][i] ^= 1
        def flipCol(col):
            for i in range(len(grid)):
                grid[i][col] ^= 1

        for i in range(len(grid)):
            if grid[i][0] == 0:
                flipRow(i)

        for j in range(len(grid[0])):
            oneCnt = 0
            for i in range(len(grid)):
                oneCnt += grid[i][j]
            if oneCnt <= len(grid) // 2:
                flipCol(j)
        
        answer = 0
        for row in grid:
            mul = 1
            for j in range(len(row) - 1, -1, -1):
                answer += (row[j]) * mul
                mul *= 2

        return answer
