class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        area = 0
        n = len(grid)

        for i in range(n):

            area += max(grid[i])      # Front view

            for j in range(n):
                if grid[i][j] > 0:
                    area += 1          # Top view

        for j in range(n):

            mx = 0

            for i in range(n):
                mx = max(mx, grid[i][j])

            area += mx                # Side view

        return area