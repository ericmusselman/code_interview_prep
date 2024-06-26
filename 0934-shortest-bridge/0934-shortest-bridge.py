class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find land in the first Island: call it Island A
        n = len(grid)
        first_land_x, first_land_y = -1, -1
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    first_land_x, first_land_y = x, y
                    break
        
        # check that step is valid
        def is_valid(x, y, n):
            if 0 <= x < n and 0 <= y < n:
                return True
            else:
                return False
            
        # check for neighboring land of first_land_x, first_land_y and add to BFS queue
        def bfs(x, y):
            grid[x][y] = 2
            bfs_queue.append((x,y))
            for (step_x, step_y) in directions:
                tmp_x, tmp_y = x+step_x, y+step_y
                if is_valid(tmp_x, tmp_y, n) and grid[tmp_x][tmp_y] == 1:
                    bfs(tmp_x, tmp_y)
            
        bfs_queue = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # add land from Island A to bfs_queue
        bfs(first_land_x, first_land_y)
        
        distance = 0
        while bfs_queue:
            next_bfs_queue = []
            for x, y in bfs_queue:
                for (step_x, step_y) in directions:
                    tmp_x, tmp_y = x+step_x, y+step_y
                    if is_valid(tmp_x, tmp_y, n):
                        if grid[tmp_x][tmp_y] == 1:
                            return distance
                        elif grid[tmp_x][tmp_y] == 0:
                            next_bfs_queue.append((tmp_x, tmp_y))
                            grid[tmp_x][tmp_y] = -1
                            
            # reset queue at the end so we check one distance magnitude at a time
            bfs_queue = next_bfs_queue
            distance += 1
            
        
        # Time: O(n^2), Space: O(n^2)