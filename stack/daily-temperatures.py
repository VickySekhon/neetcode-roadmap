def daily_temperatures(temperatures):
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
     # TODO: O(N^2), worst case is that the high temperatures are at the beginning and the low temperatures are at the end
     result = []
     for i in range(len(temperatures)):
          for j in range(i+1, len(temperatures)):
               if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
               elif j == len(temperatures) - 1:
                    result.append(0)
     result.append(0)     
     
     return result

print(daily_temperatures([21,22,23]))


def daily_temperatures2(temperatures):
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
     stack = temperatures
     res = []
     
     i = 0
     top = 1
     while len(res) != len(temperatures)-1:
          
          if stack[top] > temperatures[i]:
               res.append(top-i)
               i+=1
               top=i+1
          
          elif top == len(stack)-1:
               res.append(0)
               i+=1
               top=i+1
          
          else:
               top+=1
     res.append(0)
     return res              
print(daily_temperatures2([21,22,23]))


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
     stack = [] # hold each temperature and its index in decreasing order
     result = [0] * len(temperatures) # initialize result to be 0
     
     for i in range(len(temperatures)):
          futureTemp = temperatures[i] # represents a future temperature after the current temperature
          
          while stack and futureTemp > stack[-1][0]: # temperature higher than the one on the top of the stack is found
               currentTemp, stackIndx = stack.pop()
               result[stackIndx] = i - stackIndx
               
          stack.append([futureTemp, i]) # append current temperature (& index) into stack because either: 1) future temperature < current temperature  or 2) future temperature > current temperature so we replace the smaller current temperature with the greater temperature
     
     return result

print(daily_temperatures2([21,22,23]))




# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

"""
temperatures = [0,0,0,0,0,0,0,0], stack = [73], 73
temperatures = [1,0,0,0,0,0,0,0], stack = [74], 74, 1 pop, temperatures[?] = 1
temperatures = [1,1,0,0,0,0,0,0], stack = [75], 75, 1 pop, temperatures[?] = 1
temperatures = [1,1,0,0,0,0,0,0], stack = [75, 71], 71
temperatures = [1,1,0,0,0,0,0,0], stack = [75, 71, 69], 69
temperatures = [1,1,0,0,0,0,0,0], stack = [75, 71, 69, 72], 72
temperatures = [1,1,0,0,0,0,0,0], stack = [76], 76, 4 pops, temperatures[?] = 4

stack, answers = [temperatures[0]], []
for i in range(1, len(temperatures)):
     temp = temperatures[i]
     distance_to_high_temp = 0
     while stack and temp > stack[-1]:
          stack.pop()
          distance_to_high_temp += 1
     answers.append(distance_to_high_temp)
     stack.append(temp)
return answers
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp = [0] * len(temperatures) 
        # for i, val in enumerate(temperatures):
        #     j = i+1
        #     while j < len(temperatures) and temperatures[j] <= val:
        #         j += 1
        #     if j < len(temperatures):
        #         temp[i] = j-i
        # return temp
        # stack, answers = [temperatures[0]], []
        # for i in range(1, len(temperatures)):
        #     temp = temperatures[i]
        #     distance_to_high_temp = 0
        #     while stack and temp > stack[-1]:
        #         stack.pop()
        #         distance_to_high_temp += 1
        #     answers.append(distance_to_high_temp)
        #     stack.append(temp)
        # return answers

        answers = [0]*len(temperatures)
        stack = []
        for current_index, current in enumerate(temperatures):
            
            while stack and current > list(stack[-1].keys())[0]: # current > top of stack
                temp_entry = stack.pop()
                temp_index = list(temp_entry.values())[0]
                answers[temp_index] = current_index - temp_index # positions away the value is
            
            stack.append({current: current_index})
        return answers