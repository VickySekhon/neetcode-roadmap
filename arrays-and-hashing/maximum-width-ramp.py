def maxWidthRamp(nums):
     """
     :type nums: List[int]
     :rtype: int
     """

     seq_lens = []

     for i in range(len(nums)):
          curr = nums[i]
          curr_seq_len = i
          for j in range(i+1, len(nums)):
               nxt = nums[j]
               if (curr <= nxt):
                    curr_seq_len = j
          seq_lens.append(curr_seq_len-i)
     
     return max(seq_lens)


print(maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))

print(maxWidthRamp([6,0,8,2,1,5]))



def maxWidthRampOptimal(nums):
     """
     :type nums: List[int]
     :rtype: int
     """

     stack = []
     
     for i in range(len(nums)):
          if not stack or nums[i] < nums[stack[-1]]:
               stack.append(i)
          
     max_width = 0
     for i in range(len(nums)-1, -1, -1):
          while stack and nums[i] >= nums[stack[-1]]:
               max_width = max(max_width, i-stack.pop())
               
     return max_width

print(maxWidthRampOptimal([9,8,1,0,1,9,4,0,4,1]))


class hashMap: 
     def __init__(self):
          self.map = {}
     
     def insert(self, key, value):
          self.map[key] = value
     
     def get(self, key):
          return self.map[key]
     
     def delete(self, key):
          del self.map[key]
     
     def contains(self, key):
          return key in self.map
     

class Person: 
     name = ""
     age = 0 
     
     def __init__(self, name, age):
          self.name = name
          self.age = age
          
     def __str__(self):
          return self.name + " " + str(self.age)
     
     def __repr__(self):
          return self.name + " " + str(self.age)
     
     def __eq__(self, other):
          return self.name == other.name and self.age == other.age
     
     def __hash__(self):
          return hash((self.name, self.age))
     