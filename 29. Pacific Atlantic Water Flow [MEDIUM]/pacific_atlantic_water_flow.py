class Solution:
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
        


        