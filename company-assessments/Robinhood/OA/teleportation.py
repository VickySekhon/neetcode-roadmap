"""
You are given:

A 2D grid defined by:

height (number of rows)

width (number of columns)

A starting position inside the grid (row, col).

A string of moves made up of characters:

"D" → move down

"U" → move up

"R" → move right

"L" → move left

Two special grid positions:

teleport_a

teleport_b

These two positions are linked:

If you step on teleport_a, you instantly move to teleport_b

If you step on teleport_b, you instantly move to teleport_a

You must:

Process the moves in order.

Update the position after each move.

Apply teleportation immediately if you land on one of the teleport tiles.

Ensure movement stays within grid bounds.

Return the final position as a list of two integers: [row, col].

"""
def compute_final_position(
    height: int,
    width: int,
    position: list[int],
    moves: str,
    teleport_a: list[int],
    teleport_b: list[int]
) -> list[int]:
     dirs = {
          "U": [-1,0],
          "D": [1, 0],
          "L": [0,-1],
          "R": [0, 1],
     }
     
     for dir in moves:
          move = dirs[dir]
          new_pos = [position[0] + move[0], position[1] + move[1]]
          
          if new_pos[0] >= height or new_pos[0] < 0:
               print("OUT OF BOUNDS (ROW)")
               continue
          elif new_pos[1] >= width or new_pos[1] < 0:
               print("OUT OF BOUNDS (COL)")
               continue
          
          if new_pos == teleport_a:
               position = teleport_b
          elif new_pos == teleport_b:
               position = teleport_a
          else:
               position = new_pos
     return position


# x = compute_final_position(4, 4, [0,0], "DDLDRDL", [0,2], [3,1])
# print(x)

# No teleport used
assert compute_final_position(
    height=5,
    width=5,
    position=[2, 2],
    moves="RRU",
    teleport_a=[0, 0],
    teleport_b=[4, 4]
) == [1, 4]
# Step on teleport_a and jump to teleport_b
assert compute_final_position(
    height=5,
    width=5,
    position=[1, 1],
    moves="R",
    teleport_a=[1, 2],
    teleport_b=[3, 3]
) == [3, 3]
# Step on teleport_b and jump to teleport_a
assert compute_final_position(
    height=5,
    width=5,
    position=[2, 2],
    moves="D",
    teleport_a=[1, 1],
    teleport_b=[3, 2]
) == [1, 1]
assert compute_final_position(
    height=3,
    width=3,
    position=[0, 0],
    moves="UUULL",
    teleport_a=[1, 1],
    teleport_b=[2, 2]
) == [0, 0]
assert compute_final_position(
    height=5,
    width=5,
    position=[2, 1],
    moves="R",
    teleport_a=[2, 2],
    teleport_b=[0, 0]
) == [0, 0]
""" 

idea:

iterate through directions

see if direction + current position (without overwriting current position) is off the grid
     (these are indexes):
     - row >= height or row < 0
     - col >= width or col < 0

     if yes: do nothing
     if no: 
          check if position is a teleport spot:
               position == spot_b:
                    position = spot_a
               position == spot_a:
                    position = spot_b     

          if no:
               update position

pseudocode:

     dirs = {
          "D": [1, 0]
          "U": [-1, 0]
          "L": [0, -1]
          "R": [0, 1]
     }
     for dir in moves:
          move = dirs[dir]
          new_pos = [position[0] + move[0], position[1] + move[1]]
          if new_pos[0] >= height or new_pos[0] < 0:
               continue
          elif new_pos[1] >= width or new_pos[1] < 0:
               continue
          
          if new_pos == teleport_a:
               position = teleport_b
          elif new_pos == teleport_b:
               position = teleport_a
          else:
               position = new_pos
     return position
          
          
               
          
          
          
          
"""