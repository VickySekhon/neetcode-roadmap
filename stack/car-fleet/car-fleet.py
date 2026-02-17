def car_fleet_problem(target, position, speed):
     """
     Calculates the number of car fleets that can reach the target destination.

     Args:
          cars (List[int]): List of positions of cars on a road.
          target (int): Target position on the road.

     Returns:
          int: Number of car fleets that can reach the target.

     Raises:
          ValueError: If the length of the cars list is not equal to the length of the target list.

     Example:
          >>> car_fleet_problem([4,1,0,7], 10, [2,2,1,1])
          3
     """
     # collision = if a car behind another car reaches that car before or during when the car infront reaches the finish line in the same # of steps (time)
     # mathematically a collision = time (x) two cars reach the same position (y)
     # stack behavior = contains the # of steps a car behind another car will need before reaching the finish line (helps keep track of collisions)
     cars = [[p,s] for p,s in zip(position, speed)]
     # create array containing cars starting position (b) and their speeds (m) in sorted order
     cars.sort()
     stack = []
     for i in cars[::-1]:
          position = i[0]
          speed = i[1]
          
          stack.append((target - position) / speed) # steps it takes car at position (b) to reach finish line
          if len(stack) >= 2 and collision(stack[-1], stack[-2]): # we have a collision because the car behind is faster than the one in front
               stack.pop()
               
     return len(stack)

def collision(carB, carA):
     return carB <= carA

positions = [6,8]
target = 10
speeds = [3,2]
print(car_fleet_problem(target, positions, speeds))
print(car_fleet_problem(20, [6,2,17], [3,9,2]))




class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pos_to_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_to_speed.sort(key = lambda x : x[0], reverse=True)

        for pos, speed in pos_to_speed:
            time = (target-pos)/speed
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)