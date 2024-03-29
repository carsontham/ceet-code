# Qns : Number of Islands https://leetcode.com/problems/number-of-islands/

# Approach: using Depth-First-Search
1) In 2D matrix, iterate through each element. If it's = '1', increment island, mark it as '0'.
2) use a interative approach to mark connecting elements as '0'
3) return the island
4) create a array of tuples to store the direction to visit, up down left right
---

# Solution:
```
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
```
---

# Time Complexity
Time complexity is O(R*C). have to loop through each element in the grid.

# Space Complexity
Space complexity is O(1), if not counting stack frames.