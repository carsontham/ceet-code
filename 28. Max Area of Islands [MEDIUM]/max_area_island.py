class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def findArea(grid, r, c):
            if ( 0<= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == 1:
                grid[r][c] = 0

                area = 1

                for row_inc, col_inc in direction:
                    area += findArea(grid, r + row_inc, c + col_inc)

                return area
            
            else:
                return 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                area = findArea(grid, row, column)
                maxArea = max(maxArea, area)
        return maxArea