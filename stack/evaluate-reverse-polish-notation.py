import math
def evaluate_reverse_polish_notation(tokens):
     """
     Evaluates the given list of tokens in Reverse Polish Notation (RPN) and returns the result.

     Args:
          tokens (list): A list of strings representing the RPN expression.

     Returns:
          int or float: The result of evaluating the RPN expression.

     Raises:
          ValueError: If the RPN expression is invalid or cannot be evaluated.
     """
     # Implementation code goes here
     operators = ["+", "-", "*", "/"]
     stack = []
     for i in tokens:
          # operator
          if i in operators:
               op2, op1 = stack.pop(), stack.pop()
               result = eval(op1 + i + op2)
               stack.append(str(int(result))) # append the value into the stack as a string after truncating it towards 0 using int()
          # non-operator => either a valid num or invalid char
          elif not i.isalpha():
               stack.append(i)
     return int(stack[-1])

print(evaluate_reverse_polish_notation(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

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
     # TODO: TC: O(2*N) because we are iterating through each value in tokens, adding it to the stack, and removing it from the stack
     # TODO: SC: O(N) because a stack must be created that has n elements in the worst case (operators appear after operands in the tokens array)
     stack = []    
     for i in tokens:
          if i == "+":
               stack.append(stack.pop() + stack.pop())
          elif i == "-":
               op2, op1 = stack.pop(), stack.pop()
               stack.append(op1 - op2)
          elif i == "*":
               stack.append(stack.pop() * stack.pop())
          elif i == "/":
               op2, op1 = stack.pop(), stack.pop()
               stack.append(int(op1 / op2))
          else:
               stack.append(int(i))
     return stack[0]
print(evaluate_reverse_polish_notation2(tokens = ["10","6","9","3", "+", "-", "/"]))