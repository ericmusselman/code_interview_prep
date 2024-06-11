class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        # perform BFS starting from all 0's, and keep track of distance
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1)) # 1 step away
                    seen.add((row, col))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps+1))
                    mat[next_row][next_col] = steps
        return mat
                    