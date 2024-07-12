def longest_consecutive_sequence(nums):
     """
     Finds the length of the longest consecutive sequence in a given list of integers.

     Args:
          nums (List[int]): A list of integers.

     Returns:
          int: The length of the longest consecutive sequence.

     Example:
          >>> longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
          4
     """
     # Implementation code goes here
     nums.sort()

     arr = []
     lengths = []
     for i in range(len(nums)):
          if (len(arr) == 0):
               arr.append(nums[i])
          else:
               if (arr[-1] + 1 == nums[i]):
                    arr.append(nums[i])
               elif (arr[-1] == nums[i]):
                    continue 
               else:
                    lengths.append(len(arr))
                    arr = [nums[i]]

     lengths.append(len(arr))
     
     return max(lengths)

print(longest_consecutive_sequence(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))


def longest_consecutive_sequence2(nums):
     """
     Finds the length of the longest consecutive sequence in a given list of integers.

     Args:
          nums (List[int]): A list of integers.

     Returns:
          int: The length of the longest consecutive sequence.

     Example:
          >>> longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
          4
     """
     # Implementation code goes here
     numSet = set(nums) # eliminate duplicates
     maxSeqLen = 0
     
     for i in numSet:
          if not i-1 in numSet: # start of a sequence
               currSeqLen = 1
               while i+currSeqLen in numSet:
                    currSeqLen += 1
               maxSeqLen = max(maxSeqLen, currSeqLen)
     return maxSeqLen

print(longest_consecutive_sequence2([0,3,7,2,5,8,4,6,0,1]))
