def contains_duplicate(nums):
     """
     Checks if a list of numbers contains any duplicates.

     Args:
          nums (list): A list of numbers.

     Returns:
          bool: True if the list contains duplicates, False otherwise.
     """
     
     hashMap = {}
     
     for i in range(len(nums)):
          if (not nums[i] in hashMap):
               hashMap[nums[i]] = 1
          else:
               hashMap[nums[i]] += 1
               
     for i in hashMap.values():
          if i > 1:
               return True
     
     return False

     # TODO: solution 2
     arr = {}
     
     for i in nums:
          if i in arr:
               return True
          arr[i] = 1

     return False


print(contains_duplicate([1,2,3,3]))