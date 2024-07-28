function carFleet(target: number, position: number[], speed: number[]) {
     /*
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
     */
     let cars: any = [];
     for (let i = 0; i < position.length; i++) {
          cars.push([position[i], speed[i]]);
     }
     cars.sort((a,b) => a[0]-b[0]);
     let stack: any = []; 

     console.log(cars);

     for (let i = cars.length-1; i >= 0; i--) {
          const carPosition = cars[i][0];
          const carSpeed = cars[i][1];
          const collisionPoint = (target - carPosition) / carSpeed
          stack.push(collisionPoint);
          console.log(stack);
          if (stack.length >= 2) {
               const firstCar = stack[stack.length - 1];
               const secondCar = stack[stack.length - 2];
               if (firstCar <= secondCar)
                    stack.pop();
          }
     }
     return stack.length;
}


console.log(carFleet(20,[6,2,17], [3,9,2]))
