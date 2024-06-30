class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def which_box(row, col, n):
            return (row // n)*n + col // n
        
        def place_check(val, row, col, n):
            return not (
                val in rows[row]
                or val in cols[col]
                or val in boxes[which_box(row, col, n)]
            )
        
        def place(row, col, val, n):
            rows[row].add(val)
            cols[col].add(val)
            boxes[which_box(row, col, n)].add(val)
            board[row][col] = str(val)
        
        def remove(row, col, val, n):
            rows[row].remove(val)
            cols[col].remove(val)
            boxes[which_box(row, col, n)].remove(val)
            board[row][col] = "."
        
        def place_next(row, col):
            if col == N - 1 and row == N - 1:
                solved[0] = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
        
        def backtrack(row=0, col=0, n=3):
            if board[row][col] == ".":
                for val in range(1,n*n+1):
                    if place_check(val, row, col, n):
                        place(row, col, val, n)
                        place_next(row, col)
                        if solved[0]:
                            return
                        remove(row, col, val, n)
            else:
                place_next(row, col)
        
        n = 3
        N = n*n
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if board[row][col] != ".":
                    val = int(board[row][col])
                    place(row, col, val, n)
        solved = [False]
        backtrack()