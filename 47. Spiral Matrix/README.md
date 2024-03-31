# Qns : Spiral Matrix https://leetcode.com/problems/spiral-matrix/

# Approach
1) Use a while loop to spiral around the matrix
2) Straightforward but have to be careful with the index boundaries

# Solution:
```
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # iterate top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # iterate right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # iterate bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # iterate left column 
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
```
---

# Time Complexity
Time complexity is O(n*m), iterate through entire matrix.

# Space Complexity
Space complexity is O(m*n), store all elements.