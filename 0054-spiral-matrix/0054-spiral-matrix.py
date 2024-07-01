class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1
        row, col = 0, 0
        output = []
        
        while len(output) < m*n:
            
            for col in range(left, right + 1):
                output.append(matrix[top][col])
            
            for row in range(top + 1, bottom + 1):
                output.append(matrix[row][right])
            
            if top != bottom:
                for col in range(right-1, left-1, -1):
                    output.append(matrix[bottom][col])
            
            if left != right:
                for row in range(bottom - 1, top, -1):
                    output.append(matrix[row][left])
                    
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            
        return output
            