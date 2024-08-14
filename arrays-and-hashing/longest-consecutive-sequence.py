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
     # TODO: O(nlog(n))
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

print(sorted([100, 4, 200, 1, 3, 2]))
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
     # TODO: O(n)
     numSet = set(nums) # eliminate duplicates
     maxSeqLen = 0
     
     for i in numSet:
          if not i-1 in numSet: # start of a sequence
               currSeqLen = 1 # one number currently in the sequence
               while i+currSeqLen in numSet:
                    currSeqLen += 1
               maxSeqLen = max(maxSeqLen, currSeqLen)
     return maxSeqLen

print(longest_consecutive_sequence2([0,3,7,2,5,8,4,6,0,1]))

# create a set from the nums, check if a num is a start of a new sequence (it-1 is not in the hashMap), if it is then set up a temp counter = 1 and while i +counter in hashMap, count+=1



def longest_consecutive_sequence3(nums):
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
    maxSeqLen = 0
    nums = set(nums) # remove duplicates (1,1,2,3)
    
    for num in nums:
        if not num-1 in nums: # find start of sequence
            seqLen = 1
            while num+seqLen in nums:
                seqLen+=1
            maxSeqLen = max(maxSeqLen, seqLen)
    return maxSeqLen
 
#O(N) space, set in worst case can take up n slots assuming each num in nums is distinct
#O(N) complexity, only entering O(N) for select few nums and not repeating <= (KEY)
print(longest_consecutive_sequence3(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))