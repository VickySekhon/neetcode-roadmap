def is_valid_sudoku(board):
     """
     Check if a given Sudoku board is valid.

     Args:
          board (list): A 9x9 Sudoku board represented as a list of lists.

     Returns:
          bool: True if the Sudoku board is valid, False otherwise.
     """
     # Implementation code goes here
     return valid_rows(board) and valid_columns(board) and valid_subgrids(board)

def valid_rows(board):
     hashMap = {}
     
     for row in board:
          for num in row:
               if (num != "."):
                    if (num in hashMap):
                         return False
                    else:
                         hashMap[num] = 1
          hashMap.clear()
               
     return True

def valid_columns(board):
     
     hashMap = {}
     colIndx = 0
     
     while (colIndx < 9): 
          for row in board:
               if (row[colIndx] != "."):
                    if (row[colIndx] in hashMap):
                         return False
                    else:
                         hashMap[row[colIndx]] = 1
          
          hashMap.clear()
          colIndx += 1
          
     return True

def valid_subgrids(board):
     return
          

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".","2","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(valid_columns(board))