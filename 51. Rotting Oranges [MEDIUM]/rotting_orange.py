class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use a deque to store rotten oranges indexes
        q = deque()
        global fresh
        # count the number of total fresh oranges
        fresh = 0

        # first loop is to add all rotten oranges to deque()
        # and also count the number of fresh oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
                if grid[row][col] == 1:
                    fresh += 1 

        # initialize the minute as 0 and prev as the number of fresh oranges
        minute = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def mark_orange_rotten(grid, r, c):
            global fresh
            # update all neighbour orange to rotte (2) if they are fresh (1)
            for row_inc, col_inc in directions:
                cur_r, cur_c = r + row_inc, c + col_inc
                if 0 <= cur_r < len(grid) and 0 <= cur_c < len(grid[0]) and grid[cur_r][cur_c] == 1:
                    grid[cur_r][cur_c] = 2
                    # decrement fresh count
                    fresh -= 1

                    # now append the new rotten orange
                    q.append((cur_r,cur_c, minute +1))


        # while rotten oranges exists in the grid
        while q:
            # settle the items in the deque() by popping them
            row, col, minute = q.popleft()
            if grid[row][col] == 2:
                mark_orange_rotten(grid, row, col)
    
        # while loop breaks when q is empty
        
        if fresh > 0:
            return -1
        else:
            return minute

