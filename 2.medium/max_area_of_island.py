# https://leetcode.com/problems/max-area-of-island/

class Solution:

    """
    Runtime 25 ms Beats 50.40%
    """
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        islands = []
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited:
                    continue
                if grid[r][c] == 0:
                    continue
                queue = [(r, c)]
                temp = []
                while queue:
                    curr = curr_r, curr_c = queue.pop(0)
                    temp.append(curr)
                    visited.add((r, c))
                    for d in dirs:
                        n = next_r, next_c = curr_r + d[0], curr_c + d[1]
                        if not (0 <= next_r < rows and 0 <= next_c < cols):
                            continue
                        if n in visited:
                            continue
                        if grid[next_r][next_c] == 0:
                            continue
                        queue.append(n)
                        visited.add(n)
                islands.append(len(temp))

        if not islands:
            return 0
        return max(islands)
