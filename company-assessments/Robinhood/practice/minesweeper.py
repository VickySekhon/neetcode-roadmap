class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        Input: 
        board = [
                ["E","E","E","E","E"]
                ["E","E","M","E","E"]
                ["E","E","E","E","E"]
                ["E","E","E","E","E"]
                ]
        click = [3,0]
                [
                ["B","1","E","1","B"],
                ["B","1","M","1","B"],
                ["B","1","1","1","B"],
                ["B","B","B","B","B"]
                ]


        [
                ["E","E","E","E","E"]
                ["B","1","M","E","E"]
                ["B","B","B","E","E"]
                ["B","B","B","E","E"]
        ]
        """
        dirs = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1],[-1,1], [1,-1]]
        
        row_click, col_click = click[0], click[1]
        m, n = len(board), len(board[0])

        if board[row_click][col_click] == "M" or board[row_click][col_click] == "X":
            board[row_click][col_click] = "X"
            return board
        
        num = 0
        for direc in dirs:
            row, col = direc
            new_row = row_click + row
            new_col = col_click + col

            if (new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and board[new_row][new_col] == "M"):
                num += 1

        if num > 0:
            board[row_click][col_click] = str(num)
            return board
        

        board[row_click][col_click] = "B"
        for direc in dirs:
            row, col = direc
            new_row = row_click + row
            new_col = col_click + col

            if (new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and board[new_row][new_col] == "E"):
                self.updateBoard(board, [new_row, new_col])

        return board