def find_smallest_missing_integer(nums) -> int:
     """
     Finds the smallest missing positive integer from the given list of integers.

     Args:
          nums (List[int]): A list of integers.

     Returns:
          int: The smallest missing positive integer.

     Raises:
          ValueError: If the list is empty or contains non-positive integers only.

     """
     # use a set to only represent unique numbers
     unique = set(nums)
     
     smallest = 1
     while smallest in unique:
          smallest+=1
     return smallest

print(find_smallest_missing_integer([1,2,4,5,6,8]))



def find_smallest_missing_integer2(nums) -> int:
     """
     Finds the smallest consecutive positive integer that is missing from the 
     given list of integers.

     Args:
          nums (List[int]): A list of integers.

     Returns:
          int: The smallest missing positive integer.

     Raises:
          ValueError: If the list is empty or contains non-positive integers only.
     """
     
     unique = set(nums)
     
     smallest = 1 #smallest positive number
     while smallest in unique:
          smallest+=1
     return smallest

print(find_smallest_missing_integer2([1,2,3,4,5,6,9]))