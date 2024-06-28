class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = []
        
        for row in range(numRows):
            
            tmp = [None for _ in range(row+1)]  # row to fill in and then add
            tmp[0], tmp[-1] = 1, 1
            
            for col in range(1, len(tmp)-1):
                tmp[col] = triangle[row-1][col-1] + triangle[row-1][col]
                
            triangle.append(tmp)
        
        return triangle
        
        # Time: numRows^2, Space: O(1)
        