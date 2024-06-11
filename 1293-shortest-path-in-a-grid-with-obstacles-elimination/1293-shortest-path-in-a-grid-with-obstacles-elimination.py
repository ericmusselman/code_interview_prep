class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # use variable to keep track of how many obstacle removals "remain", for valid step force to be >0
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        m = len(grid)
        n = len(grid[0])
        queue = deque([(0, 0, k, 0)]) # k removals remaining, 0 steps
        seen = {(0, 0, k)} # k removals remaining
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, remain, steps = queue.popleft()
            
            # if we found bottom right corner
            if row == m-1 and col == n-1:
                return steps
            
            # otherwise, iterate over the neighbors
            for dx, dy in directions:
                next_row, next_col = row+dy, col+dx
                if valid(next_row, next_col):
                    # open space (not obstacle)
                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col, remain) not in seen:
                            seen.add((next_row, next_col, remain))
                            queue.append((next_row, next_col, remain, steps+1))
                    
                    # obstacle, check if enough removals left
                    elif remain and (next_row, next_col, remain-1) not in seen:
                        seen.add((next_row, next_col, remain-1))
                        queue.append((next_row, next_col, remain-1, steps+1))
        
        return -1
        