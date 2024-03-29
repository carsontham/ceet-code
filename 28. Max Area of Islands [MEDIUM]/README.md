# Qns : Max Area of Islands https://leetcode.com/problems/number-of-islands/

# Approach: using Depth-First-Search
1) In 2D matrix, iterate through each element. If it's = '1', mark it as '0'.
2) use a interative approach to mark connecting elements as '0'
3) return the island
4) create a array of tuples to store the direction to visit, up down left right
5) use FindArea() method to recursively find the total area
---

# Solution:
```
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
```
---

# Time Complexity
Time complexity is O(R*C). have to loop through each element in the grid.

# Space Complexity
Space complexity is O(1), if not counting stack frames.