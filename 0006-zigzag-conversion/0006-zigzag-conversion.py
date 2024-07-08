class Solution:
    def convert(self, s: str, numRows: int) -> str:
        builder = []
        
        # go down column, -1 row at each step
        # go up and right, +1 col and -1 row at each step
        # (repeat)
        
        if numRows == 1:
            return s
        
        row, col = 0, 0
            
        nLetters = len(s)
        
        sections = ceil(nLetters / (2 * numRows - 2))
        numCols = sections * (numRows - 1)            
        
        builder = [[" "] * numCols for _ in range(numRows)]
        n = 0
        while n < nLetters:
            # go down column, +1 row at each step
            while row < numRows and n < nLetters:
                builder[row][col] = s[n]
                n += 1
                row += 1
            
            # go up and right, +1 col and -1 row at each step
            col += 1
            row -= 2
            while row > 0 and col < numCols and n < nLetters:
                builder[row][col] = s[n]
                n += 1
                row -= 1
                col += 1
        
        output = ""
        for row in builder:
            output += "".join(row)

        return output.replace(" ", "")
            