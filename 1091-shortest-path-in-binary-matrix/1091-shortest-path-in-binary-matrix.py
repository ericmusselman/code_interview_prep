class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        n = len(grid)
        queue = deque([(0, 0, 1)])  # (row, col, distance)
        seen = {(0, 0)}
        steps = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        
        while queue:
            (row, col, distance) = queue.popleft()
            # if we are in the lower-right corner
            if (row, col) == (n-1, n-1):
                return distance
            
            for x, y in steps:
                step_x, step_y = row+y, col+x
                
                if valid(step_x, step_y) and (step_x, step_y) not in seen:
                    seen.add((step_x, step_y))
                    queue.append((step_x, step_y, distance + 1))
        return -1
    