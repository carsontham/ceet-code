class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def set_island_zero(grid, row, column):
            if ( 0<= row < len(grid)) and (0 <= column < len(grid[0])) and grid[row][column] == "1":
                grid[row][column] = "0"

                for row_inc, column_inc in directions:
                    set_island_zero(grid, row+row_inc, column+column_inc)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    island += 1
                    
                    set_island_zero(grid, row, column)
        
        return island
    