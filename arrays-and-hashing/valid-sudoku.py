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
     arr1 = []
     arr2 = []
     arr3 = []
     
     for row in range(9):
          for col in range(9):
               num = board[row][col]
               if (num != "."):
                    if (col < 3):
                         if (num in arr1):
                              return False
                         arr1.append(num)
                    elif (col >= 3 and col < 6):
                         if (num in arr2):
                              return False
                         arr2.append(num)
                    else: 
                         if (num in arr3):
                              return False
                         arr3.append(num)
                         
          if (row == 2 or row == 5 or row == 8):
               arr1 = []
               arr2 = []
               arr3 = []
               
     
     return True

board = [["1","2",".",".","3",".",".",".","."],
          ["4",".",".","5",".",".",".",".","."],
          [".","9","8",".",".",".",".","2","3"],
          ["5",".",".",".","6",".",".",".","4"],
          [".",".",".","8",".","3",".",".","5"],
          ["7",".",".",".","2",".",".",".","6"],
          [".",".",".",".",".",".","2",".","."],
          [".",".",".","4","1","9",".",".","8"],
          [".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku(board))


import collections
def is_valid_sudoku2(board):
     """
     Check if a given Sudoku board is valid.

     Args:
          board (list): A 9x9 Sudoku board represented as a list of lists.

     Returns:
          bool: True if the Sudoku board is valid, False otherwise.
     """
     # Implementation code goes here
     rows = collections.defaultdict(set) # dictionary (keys: tuples, integers, strings) => set (values: set)
     cols = collections.defaultdict(set) 
     subGrids = collections.defaultdict(set)
     
     for rowIndx in range(9):
          for colIndx in range(9):
               num = board[rowIndx][colIndx]
               if (num != "."): # empty space
                    if (num in rows[rowIndx] or
                        num in cols[colIndx] or
                        num in subGrids[(rowIndx//3, colIndx//3)]):
                         return False
                    rows[rowIndx].add(num)     
                    cols[colIndx].add(num)     
                    subGrids[(rowIndx//3, colIndx//3)].add(num)
     return True

board  = [["1","2",".",".","3",".",".",".","."],
          ["4",".",".","5",".",".",".",".","."],
          [".","9","8",".",".",".",".","2","3"],
          ["5",".",".",".","6",".",".",".","4"],
          [".",".",".","8",".","3",".",".","5"],
          ["7",".",".",".","2",".",".",".","6"],
          [".",".",".",".",".",".","2",".","."],
          [".",".",".","4","1","9",".",".","8"],
          [".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku2(board))


import collections
def is_valid_sudoku3(board):
     """
     Check if a given Sudoku board is valid.

     Args:
          board (list): A 9x9 Sudoku board represented as a list of lists.

     Returns:
          bool: True if the Sudoku board is valid, False otherwise.
     """
     rows = collections.defaultdict(set)
     cols = collections.defaultdict(set)
     subgrids = collections.defaultdict(set)
     
     for rowIndx in range(len(board)):
          for colIndx in range(len(board)):
               num = board[rowIndx][colIndx]
               if (num != "."):
                    if (num in rows or
                        num in cols or
                        num in subgrids):
                         return False
                    rows[rowIndx].add(num)
                    cols[colIndx].add(num)
                    subgrids[(rowIndx//3, colIndx//3)].add(num)
     return True
     

board  = [["1","2",".",".","3",".",".",".","."],
          ["4",".",".","5",".",".",".",".","."],
          [".","9","8",".",".",".",".","2","3"],
          ["5",".",".",".","6",".",".",".","4"],
          [".",".",".","8",".","3",".",".","5"],
          ["7",".",".",".","2",".",".",".","6"],
          [".",".",".",".",".",".","2",".","."],
          [".",".",".","4","1","9",".",".","8"],
          [".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku3(board))