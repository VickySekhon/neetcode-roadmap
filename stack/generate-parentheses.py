
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
     stack = [] # track current combination
     result = [] # collection of all combinations
     
     # function that does all the work
     def backtracking(open_count, close_count):
          if open_count == close_count == n: # end of combination reached
               result.append("".join(stack))
               return

          if open_count < n: # add an open parenthesis
               stack.append("(")
               backtracking(open_count + 1, close_count)
               stack.pop()
          
          if close_count < open_count: # cannot have a close parenthesis if we do not have a open parenthesis
               stack.append(")")
               backtracking(open_count, close_count + 1)
               stack.pop()
          
     backtracking(0,0)
     return result
     

print(generate_parentheses2(20))