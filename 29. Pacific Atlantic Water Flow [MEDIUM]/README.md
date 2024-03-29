# Qns : Pacific Atlantic Water Flow https://leetcode.com/problems/pacific-atlantic-water-flow/

# Approach: using Depth-First-Search
1) start with different coordinates for alantic and pacific, initialize two different arrays
2) iterate through the rows and columns, append the starting points to the two arrays
3) use two sets and & operator to ultimately return the intersection of the two sets()
4) use directions [(1,0), (-1,0), (0,1), (0,-1)]
5) create depth-first-search algo()
6) lastly, iterate through the two arrays, passing in row column and set
7) return set1() & set2() which will give the intersection

# Solution:
```
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        pacific, atlantic = [], []
        visited_pacific, visited_atlantic = set(), set()

        for row in range(len(heights)):
            pacific.append((row,0))
            atlantic.append((row, len(heights[0])-1))
        
        for column in range(len(heights[0])):
            pacific.append((0, column))
            atlantic.append((len(heights)-1, column))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c, visited):
            visited.add((r,c))
        
            for row_inc, column_inc in directions:
                new_r, new_c = r+row_inc, c+column_inc

                if (0 <= new_r < len(heights)) and (0 <= new_c <len(heights[0])) and (heights[r][c] <= heights[new_r][new_c]) and ((new_r, new_c) not in visited):
                    dfs(new_r, new_c, visited)


        for row, column in pacific: dfs(row,column, visited_pacific)
        for row, column in atlantic: dfs(row,column, visited_atlantic)

        return visited_pacific & visited_atlantic
```
---

# Time Complexity
Time complexity is O(R*C) as we loop through each element in the grid.

# Space Complexity
Space complexity is O(R*C), since we may store all elements in the set