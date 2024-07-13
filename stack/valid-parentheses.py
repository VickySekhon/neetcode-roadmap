def is_valid_parentheses(s):
     """
     Determines whether a given string of parentheses is valid.

     Args:
          s (str): The string of parentheses to be checked.

     Returns:
          bool: True if the parentheses are valid, False otherwise.
     """
     
     hashMap = {"(":")", "[":"]", "{":"}"}
     stack = []
     
     for i in s:
          # open bracket
          if (i in hashMap):
               stack.append(i)
          # close bracket or any other character
          # if no corresponding open bracket in stack return false
          elif (len(stack) == 0 or hashMap[stack[-1]] != i):
               return False
          # close bracket that matches the open bracket in the stack
          else:
               stack.pop()
     return  len(stack) == 0

print(is_valid_parentheses("[(])"))