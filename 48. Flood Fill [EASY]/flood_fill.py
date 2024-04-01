class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        starting = image[sr][sc]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def flood_fill(image, r, c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == starting:
                image[r][c] = color

                for row_inc, col_inc in directions:
                    flood_fill(image, r+row_inc, c+col_inc)
        
        flood_fill(image, sr, sc)

        return image
        