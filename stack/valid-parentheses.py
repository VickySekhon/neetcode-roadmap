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


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        open_brackets = bracket_map.values()
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if stack:
                    if bracket_map[char] != stack[-1]: return False
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
   
   
   """ 
Given a string of characters, that can contain brackets ([, {, () return if the brackets are balanced (Boolean return type)

string = "{[()]}", return = True

string = "{[()", return = False

string = "Hello there, solve this expression: (5+10)[]{}", return = True

string = "Hello there, solve this expression: ((5+10)", return = False

string = "", return = True

solution:
1. array, treat it like a stack
stack = ["("]
string = "Hello there, solve this expression: (5+10)[]{}"

stack = ["{"]
string = "Hello there, solve this expression: {(5+10)"

constraints:
- we are not necessarily interested in alpha-numeric characters
- we should use a stack to track our last encountered open bracket

complexity:
- len(string) = n
- O(n)
"""

def balanced_brackets(s):
     stack = []
     mappings = {")": "(",
                 "]": "[",
                 "}": "{"}
     
     open_brackets = mappings.values()
     close_brackets = mappings.keys()
     for char in s:
          if char in open_brackets:
               stack.append(char)
          elif char in close_brackets:
               # 2 conditions for a False case: stack is empty and we have a close bracket, stack is not empty and we don't have the correct open bracket for the close bracket
               # The close bracket is valid
               if len(stack) == 0 or (len(stack) > 0 and mappings[char] != stack[-1]):
                    return False
               stack.pop()
     return len(stack) == 0 # Returns True if stack is empty, False if stack has open brackets without corresponding close brackets

s1 = "{[()]}" # Expected: True, Returns True
s2 = "{[()" # Expected: False, Returns False
s3 = "Hello there, solve this expression: (5+10)[]{}" # Expected: True, Returns True
s4 = "Hello there, solve this expression: ((5+10)" # Expected: False, Returns: False
s5 = "" # Expected: True, Returns: True
s6 = "]()})" # Expected: False, Returns: False

x = balanced_brackets(s1)
print(x)
               