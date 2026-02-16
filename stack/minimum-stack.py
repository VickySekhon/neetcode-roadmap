
# TODO: solution #1: O(n) built-in min() is actually O(n) but this still works due to lack of insufficient test cases
class MinStack:
     def __init__(self):
          self.stack = [] # array-based stack
          
     def push(self, val: int) -> None:
          self.stack.append(val)
          return

     def pop(self) -> None:
          self.stack.pop()
          return

     def top(self) -> int:
          return self.stack[-1]

     def getMin(self) -> int:
          minVal = min(self.stack)
          return minVal
     
# stk = MinStack()
# stk.push(3)
# stk.push(2)
# print(stk.getMin())

# TODO: solution #2: O(1) pseudo-stack for minimum values, topmost element is the smallest value in the stack
class MinStack2: 
     def __init__(self):
          self.stack = [] # array-based stack
          self.minStack = []
     
     def push(self, val):
          self.stack.append(val)
          self.minStack.append(min(self.minStack[-1], val) if len(self.minStack) != 0 else val)
          return
     
     def pop(self):
          self.stack.pop()
          self.minStack.pop()
          return
     
     def top(self):
          return self.stack[-1]
     
     def getMin(self):
          return self.minStack[-1]
     
# stack = MinStack2()
# stack.push(5)
# stack.push(2)
# stack.push(7)
# print(stack.top())
# print(stack.getMin())

# TODO: linked node implementation using two stacks
class LinkedNode:
     def __init__(self, value, next=None):
          self.value = value
          self.next = next

class LinkedStack:
     def __init__(self, top):
          self.top = LinkedNode(top)
          self.minTop = LinkedNode(top)
     
     def push(self, value):
          # regular stack
          newNode = LinkedNode(value, self.top)
          self.top = newNode
          
          # min stack 
          if self.minTop is not None:
               self.minTop = LinkedNode(min(value, self.minTop.value), self.minTop)
          else:
               self.minTop = LinkedNode(value)
     
     def pop(self)-> int:
          # regular stack
          self.top = self.top.next
          
          # min stack
          self.minTop = self.minTop.next

     def get_top(self)->int:
          return self.top.value
     
     def getMin(self)->int:
          return self.minTop.value
          
          
linkStack = LinkedStack(2)
linkStack.push(2)
linkStack.push(1)
linkStack.push(0)
linkStack.push(-1)
linkStack.push(3)

print(linkStack.getMin())
print(linkStack.get_top())
linkStack.pop()
print(linkStack.get_top())