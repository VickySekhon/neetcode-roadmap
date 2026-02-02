
""" 
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
"""

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
     low_row, hi_row = 0, len(matrix)-1
     
     while low_row <= hi_row:
          mid_row = (low_row+hi_row)//2
          
          low_col, hi_col = 0, len(matrix[mid_row]) - 1
          mid_col = 0 # Use this as a heuristic that tells us which subarray to search (left or right)
          while low_col <= hi_col:
               mid_col = (low_col+hi_col)//2
               
               if matrix[mid_row][mid_col] == target:
                    return True
               if target > matrix[mid_row][mid_col]:
                    low_col = mid_col+1
               else:
                    hi_col = mid_col-1
          
          # Search the right
          if target > matrix[mid_row][mid_col]:
               low_row = mid_row+1
          else:
               hi_row = mid_row-1
     
     return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 0
# matrix=[[1],[3]]
# target=3

print(searchMatrix(matrix, target))