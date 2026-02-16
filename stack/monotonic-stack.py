stack = []

# Decreasing
def insert(value):
     if len(stack) == 0:
          stack.append(value)
          return

     while value > stack[-1]:
          stack.pop()
     stack.append(value)
     
insert(90)
insert(80)
insert(10)
insert(30)

print(stack)