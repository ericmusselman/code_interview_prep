class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        def count_neighbors(row: int, col: int):
            tally = 0
            for x_step, y_step in directions:
                if (0 <= row+y_step < m) and (0 <= col+x_step < n):
                    if board[row+y_step][col+x_step] in [1, -1]:
                       tally += 1
            return tally
        
        for row in range(m):
            for col in range(n):
                neighbors = count_neighbors(row, col)
                val = board[row][col]
                
                # 1 -> 0 = -1
                # 0 -> 1 = 2
                
                was_live_cell = True if val in [1, -1] else False
                
                if was_live_cell and neighbors < 2:
                    board[row][col] = -1
                
                elif was_live_cell and neighbors in [2, 3]:
                    pass
                
                elif was_live_cell and neighbors > 3:
                    board[row][col] = -1
                
                elif not was_live_cell and neighbors == 3:
                    board[row][col] = 2
        
        for row in range(m):
            for col in range(n):
                val = board[row][col]
                if val == 2:
                    board[row][col] = 1
                elif val == -1:
                    board[row][col] = 0
                else:
                    continue
        
        return board
        
    # Time: O(mn), Space: O(1)
    