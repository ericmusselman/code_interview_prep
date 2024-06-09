class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        steps = [(1,0), (0,1), (-1,0), (0,-1)]
        seen = set()
        output = 0
        m = len(grid)
        n = len(grid[0])
        
        def is_land(row, col):
            # m x n
            if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                return True
            else:
                return False
            
        def dfs(row, col):
            for x_step, y_step in steps:
                m_row, n_col = row + y_step, col + x_step
                if is_land(m_row, n_col) and (m_row, n_col) not in seen:
                    seen.add((m_row, n_col))
                    dfs(m_row, n_col)
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    output += 1
                    seen.add((row, col))
                    dfs(row, col)
        return output
            