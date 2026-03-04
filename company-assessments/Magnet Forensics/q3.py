""" 
Iterate over linked list and sort in ascending order
"""

class Node:
     def __init__(self, value=0, next=None):
          self.value = value
          self.next = next
class Linked_List:
     def __init__(self, value):
          self.head = Node(value)
          self.tail = self.head
          self.count = 1
     def insert(self, value):
          self.tail.next = Node(value)
          self.tail = self.tail.next
          self.count += 1
     def __str__(self):
          s = ""
          curr = self.head
          while curr is not None:
               s += f"{curr.value} "
               curr = curr.next
          return s


     def merge_sort(self, node):
          if not node or not node.next:
               return node

          left = node
          right = self.getMid(left)
          tmp = right.next
          right.next = None
          right = tmp
          
          #print(left.value, right.value)
          left = self.merge_sort(left)
          right = self.merge_sort(right)
          
          head = self.merge(left, right)
          self.head = head
          return head
     
     def merge(self, left, right):
          print(left.value, right.value)
          new_node = Node()
          curr = new_node
          while left and right:
               if left.value <= right.value:
                    new_node.next = left
                    left = left.next
               else:
                    new_node.next = right
                    right = right.next
               new_node = new_node.next
               
          if left:
               new_node.next = left
          elif right:
               new_node.next = right
          return curr.next
     
     def getMid(self, head):
          slow = head
          fast = head
          
          while fast and fast.next:
               fast = fast.next.next
               if not fast:
                    break
               slow = slow.next
          return slow
               
          
               


ll = Linked_List(5)
ll.insert(2)
ll.insert(6)
ll.insert(4)
ll.insert(9)
ll.insert(3)
print(ll)

x = ll.merge_sort(ll.head)
print(ll)

# x = ll.getMid()
# print(x.value)
""" 
     5 2 6 4 9 3 
5 2 6            4 9 3 

5  2 6           4   4 3

   2  6              4  3



     5 2 6 4 9 3 
5 2 6            4 9 3 

5 2  6           4 9  3
                    
5  2             4  9  


l = recur
r = recur

merge(l, r)

"""

# L
# R