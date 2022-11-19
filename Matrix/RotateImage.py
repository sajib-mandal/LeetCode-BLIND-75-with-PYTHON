#   48. Rotate Image


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):   # total rotation (n - 1) = (4 - 1) = 3
                top, bottom = left, right
                topLeftVal = matrix[top][left + i]
                
                # rotate bottomLeft to topLeft
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # rotate bottomRight to bottomLeft
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # rotate topRight to bottomRight
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # rotate topLeft to topRight
                matrix[top + i][right] = topLeftVal
            left += 1
            right -= 1
           
        
        
        
        
        
        left, right = 0, len(matrix) - 1
        top, bottom = left, right
        
        while left < right and top < bottom:
            for i in range(right - left):   # total rotation (n - 1) = (4 - 1) = 3
                topLeftVal = matrix[top][left + i]
                
                # rotate bottomLeft to topLeft
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # rotate bottomRight to bottomLeft
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # rotate topRight to bottomRight
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # rotate topLeft to topRight
                matrix[top + i][right] = topLeftVal
            left += 1
            right -= 1
            top += 1
            bottom -= 1
