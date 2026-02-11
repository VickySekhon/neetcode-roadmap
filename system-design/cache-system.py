""" 
Implement a cache in Python

Cache supports (key, value) pair insertion

Cache supports lookup based on key

Cache has a capacity and when it is reached...
...the least frequently accessed key in Cache 
is removed to make room for the new addition
"""
from random import choice

class Cache:
     CAPACITY = 10
     def __init__(self):
          self.access_frequencies = {}
          self.items = {}
          self.item_count = 0
          
     def _update_access_frequency(self, key, caller):
          if caller == "put":
               if not self.access_frequencies.get(key):
                    self.access_frequencies[key] = 1
               else:
                    self.access_frequencies[key] += 1
          else:
               if not self.access_frequencies.get(key):
                    print(f"Key does not exist in the dictionary!")
                    return
               self.access_frequencies[key] += 1
     
     def put(self, key, value):
          VALUE_INDX = 1
          KEY_INDX = 0
          
          # Remove least accessed value
          if self.item_count == self.CAPACITY:
               least_accessed_key = sorted(self.access_frequencies.items(), key=lambda item : item[VALUE_INDX])[KEY_INDX][KEY_INDX]
               del self.items[least_accessed_key]
               del self.access_frequencies[least_accessed_key]
               # Item count stays constant we don't need to update it
          
          self.items[key] = value
          self._update_access_frequency(key, "put")
          
          self.item_count += 1
          
     def get(self, key):
          self._update_access_frequency(key, "get")
          return self.items[key]
     
     def __str__(self):
          representation = f"Cache View:\nItems in Cache: {self.item_count}\nKey      Value\n"
          for key, val in self.items.items():
               representation += f"{key}      {val} | Times Accessed: {self.access_frequencies[key]}\n"
          return representation
          
cache = Cache()

# generate sample data
keys = "a-b-c-d-e-f-g-h-i-j".split("-")
values = [num for num in range(0,10)]

for key, val in zip(keys, values):
     cache.put(key, val)

# Access random values
for i in range(100):
     rand_key = choice(keys)
     cache.get(rand_key)
     
print(cache)
cache.put("k", "testing")
print(cache)