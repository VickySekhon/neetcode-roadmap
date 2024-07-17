function carFleet(target, position, speed) {
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
    var cars = [];
    for (var i = 0; i < position.length; i++) {
        cars.push([position[i], speed[i]]);
    }
    cars.sort(function (a, b) { return a[0] - b[0]; });
    var stack = [];
    console.log(cars);
    for (var i = cars.length - 1; i >= 0; i--) {
        var carPosition = cars[i][0];
        var carSpeed = cars[i][1];
        var collisionPoint = (target - carPosition) / carSpeed;
        stack.push(collisionPoint);
        console.log(stack);
        if (stack.length >= 2) {
            var firstCar = stack[stack.length - 1];
            var secondCar = stack[stack.length - 2];
            if (firstCar <= secondCar)
                stack.pop();
        }
    }
    return stack.length;
}
//console.log(carFleet(10,[4,1,0,7], [2,2,1,1]))
console.log(carFleet(20, [6, 2, 17], [3, 9, 2]));
