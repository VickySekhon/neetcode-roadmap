def twoSum(nums, target):
     """
     Finds two numbers in the given list that add up to the target value.

     Args:
          nums (list): A list of integers.
          target (int): The target value.

     Returns:
          list: A list containing the indices of the two numbers that add up to the target value.
     """
     hashMap = {}
     
     for indx, val in enumerate(nums):
          valueWeNeed = target - val
          if (valueWeNeed in hashMap):
               return [indx, hashMap[valueWeNeed]]
          hashMap[val] = indx
     
     return


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))