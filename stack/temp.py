def is_valid_parentheses(s):
     """
     Determines whether a given string of parentheses is valid.

     Args:
          s (str): The string of parentheses to be checked.

     Returns:
          bool: True if the parentheses are valid, False otherwise.
     """
     ht = {"(":")", "[":"]", "{":"}"}
     stack = []
     
     for i in s:
          if i in ht:
               stack.append(i)
          elif len(stack) == 0 or ht[stack[-1]] != i:
               return False
          else:
               stack.pop()
     
     return len(stack) == 0

print(is_valid_parentheses("{()}}"))


def generate_parentheses2(n):
     """
     Generates all valid combinations of n pairs of parentheses.

     Args:
          n (int): The number of pairs of parentheses.

     Returns:
          List[str]: A list of strings representing all valid combinations of parentheses.

     Example:
          >>> generate_parentheses(3)
          ['((()))', '(()())', '(())()', '()(())', '()()()']
     """
     # n open, n close
     # 3 conditions: 1) open_count > close_count then append a close bracket, 2) open_count == close_count == n then join the stack elements and stop, 3) if close_count > open_count then append open bracket
     stack = []
     result = []
     
     def backtracking(open_count, close_count):
          if open_count == close_count == n:
               result.append("".join(stack))
               return
          
          if open_count < n:
               stack.append("(")
               backtracking(open_count+1, close_count)
               stack.pop()
          
          if close_count < open_count:
               stack.append(")")
               backtracking(open_count, close_count+1)
               stack.pop()
          
          return
     
     backtracking(0,0)
     
     return result

print(generate_parentheses2(3))


def daily_temperatures3(temperatures):
     """
     This function takes in a list of daily temperatures and returns a new list where, for each day in the input list, it tells you how many days you would have to wait until a warmer temperature. If there is no future day with a warmer temperature, the corresponding value in the output list is 0.

     Parameters:
     - temperatures (list): A list of integers representing the daily temperatures.

     Returns:
     - list: A new list where each element represents the number of days you would have to wait until a warmer temperature.

     Example:
     >>> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
     [  , 1, 4, 2, 1, 1, 0, 0]
     """
     # stack will hold a temperature, indx pair
     # if you see a smaller temperature, simply push it onto the stack
     # if you see a larger temperature, while you have something in the stack and its smaller than the future temperature, compute the difference between their indices and write it to the indx of the current temperature, then pop() the current temperature and push the higher temperature to keep the monotonic order of the stack
     stack = []
     result = [0] * len(temperatures)
     
     for futIndx in range(len(temperatures)):
          futTemp = temperatures[futIndx]
          while len(stack) != 0 and futTemp > stack[-1][0]:
               currTemp, currIndx = stack.pop()
               result[currIndx] = futIndx - currIndx
          stack.append([futTemp, futIndx])
     
     return result

print(daily_temperatures3([73, 74, 75, 71, 69, 72, 76, 73]))


def evaluate_reverse_polish_notation2(tokens):
     """
     Evaluates the given list of tokens in Reverse Polish Notation (RPN) and returns the result.

     Args:
          tokens (list): A list of strings representing the RPN expression.

     Returns:
          int or float: The result of evaluating the RPN expression.

     Raises:
          ValueError: If the RPN expression is invalid or cannot be evaluated.
     """
     # division always truncates to zero
     stack = []
     
     for i in tokens:
          if i == "+":
               stack.append(stack.pop() + stack.pop())
          elif i == "*":
               stack.append(stack.pop() * stack.pop())
          elif i == "-":
               op2, op1 = stack.pop(), stack.pop()
               stack.append(op1 - op2)
          elif i == "/":
               op2, op1 = stack.pop(), stack.pop()
               stack.append(int(op1/op2))
          else:
               stack.append(int(i))
     return stack[-1]

print(evaluate_reverse_polish_notation2(["2", "3", "+"]))




class minStack:
     def __init__(self):
          self.stack = []
          self.minStack = []
          
     def pop(self):
          self.stack.pop()
          self.minStack.pop()
          
     def push(self, val):
          self.stack.append(val)
          self.minStack.append(min(self.minStack[-1], val)) if len(self.minStack) != 0 else self.minStack.append(val)
          
     def top(self):
          return self.stack[-1]
     
     def getMin(self):
          return self.minStack[-1]
     
stck = minStack()
stck.push(-1)
stck.push(3)
stck.push(1)
print(stck.getMin())



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
     # go through the list backwards, associate each car with the distance it needs to reach the target, if a car behind has a step > the car infront, it will eventually catch-up
     # stack holds the cars. If a car has a higher step than the one in the stack, 
     # monotonic stack
     cars = [[p,s] for p,s in zip(position, speed)]
     
     cars.sort()

     stack = []
     
     for i in cars[::-1]:
          pos = i[0]
          vel = i[1]
          stack.append((target-pos) / vel)
          if (len(stack) >= 2 and stack[-1] <= stack[-2]):
               stack.pop()
          
          
               
     
     return len(stack)

print(car_fleet_problem(10, [4,1,0,7], [2,2,1,1]))