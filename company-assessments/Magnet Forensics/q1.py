"""
Given an array, count how many elements at index i are divisible by the element at index i+1, where i+1 is a valid index within the array. Return the total count of such divisible elements.
"""

def divisible_count(nums):
     count = 0
     i, j, n = 0, 1, len(nums)
     
     while j < n:
          if nums[i] % nums[j] == 0:
               count += 1
          i += 1
          j += 1
     
     return count

nums = [2,4,16,32,64][::-1]
x = divisible_count(nums)
print(x)