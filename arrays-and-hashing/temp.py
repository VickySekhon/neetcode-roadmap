def contains_duplicate(nums):
     """
     Checks if a list of numbers contains any duplicates.

     Args:
          nums (list): A list of numbers.

     Returns:
          bool: True if the list contains duplicates, False otherwise.
     """
     hashMap = {} # store num-frequency
     
     for i in nums:
          if i in hashMap:
               return True
          hashMap[i] = 1
     
     return False

print(contains_duplicate([1,2,3,3]))








def validAnagram(s, t):
     """
     Checks if two strings, s and t, are anagrams of each other.

     An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
     In this case, we are checking if the characters in s can be rearranged to form t.

     Args:
          s (str): The first string.
          t (str): The second string.

     Returns:
          bool: True if s and t are anagrams, False otherwise.
     """
     
     if len(s) != len(t):
          return False
     
     hashMapS = {}
     hashMapT = {}
     
     for i in range(len(s)): # add to the hash map 
          hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
          hashMapT[t[i]] = 1 + hashMapT.get(t[i], 0)
          
     for j in hashMapS: # compare frequency of elements in each hashMap
          if (hashMapS[j] != hashMapT.get(j)):
               return False
          
     return True

s = "cat"
t = "car"
print(validAnagram(s,t))










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
     
     for i,v in enumerate(nums):
          valueWeNeed = target - v
          if (valueWeNeed in hashMap):
               return [i, hashMap[valueWeNeed]]
          hashMap[v] = i
     return

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))







def group_anagrams(words):
     """
     Groups a list of words into anagrams.

     Parameters:
     words (list): A list of strings representing words.

     Returns:
     list: A list of lists, where each inner list contains words that are anagrams of each other.
     """
     
     hashMap = {}
     result = []
     
     for word in words:
          wordSorted = "".join(sorted(word))
          if (hashMap.get(wordSorted, 0) != 0):
               hashMap[wordSorted].append(word)
          else:
               hashMap[wordSorted] = [word]
     
     for groupedAnagrams in hashMap.values():
          result.append(groupedAnagrams)
          
     return result
          
          
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))











def k_frequent_elements(nums, k):
     """
     Returns the k most frequent elements in the given list.

     Args:
          nums (List[int]): The input list of integers.
          k (int): The number of most frequent elements to return.

     Returns:
          List[int]: The k most frequent elements in the input list.
     """
     hashMap = {}
     arr = [[] for i in range(-1,len(nums))]
     
     for i in nums:
          hashMap[i] = 1 + hashMap.get(i, 0)
          
     for v,f in hashMap.items():
          arr[f].append(v)
     
     result = []
     
     for i in range(len(arr)-1, -1, -1):
          if (len(arr) != 0):
               for j in arr[i]:
                    result.append(j)
                    if (len(result) == k):
                         return result
               
     return arr

nums = [1,2,2,3,3,3,3]
k = 2
print("k frequent elements", k_frequent_elements(nums,k))






def productExceptSelf4(nums):
     """
     Calculates the product of array except self.

     Args:
          nums (int[]): The input array of integers.

     Returns:
          int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     prefix = [1]*len(nums)
     postfix = [1]*len(nums)
     
     # compute prefixes
     for i in range(1, len(nums)):
          prefix[i] = prefix[i-1] * nums[i-1]
     
     # compute postfixes
     for i in range(len(nums)-2, -1, -1):
          postfix[i] = postfix[i+1] * nums[i+1]
          
     # cross-multiply
     ctr = 0
     result = []
     
     while ctr < len(prefix):
          result.append(prefix[ctr]*postfix[ctr])
          ctr+=1
      
     return result


print("**CORRECT**: ", productExceptSelf4([-1,0,1,2,3])) 




import collections
def is_valid_sudoku2(board):
     """
     Check if a given Sudoku board is valid.

     Args:
          board (list): A 9x9 Sudoku board represented as a list of lists.

     Returns:
          bool: True if the Sudoku board is valid, False otherwise.
     """
     # Implementation code goes here
     
     rows = collections.defaultdict(set) # use a set to eliminate duplicates
     columns = collections.defaultdict(set) # use a set to eliminate duplicates
     subGrids = collections.defaultdict(set) # use a set to eliminate duplicates
     
     for row in range(9): # go through rows
          for col in range(9): # go through columns
               if (board[row][col] != "."):
                    if board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in subGrids[(row//3, col//3)]:
                         return False
                    
                    rows[row].add(board[row][col])
                    columns[col].add(board[row][col])
                    subGrids[(row//3, col//3)].add(board[row][col])
                    
     return True


board = [["1","2",".",".","3",".",".",".","."],
          ["4",".",".","5",".",".",".",".","."],
          [".","9","8",".",".",".",".","2","3"],
          ["5",".",".",".","6",".",".",".","4"],
          [".",".",".","8",".","3",".",".","5"],
          ["7",".",".",".","2",".",".",".","6"],
          [".",".",".",".",".",".","2",".","."],
          [".",".",".","4","1","9",".",".","8"],
          [".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku2(board))











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
     numbers = set(nums)
     maxSeqLen = 0
     
     for i in nums:
          if (not i-1 in nums): # start of a new sequence
               ctr = 1
               while i+ctr in numbers:
                    ctr += 1
               maxSeqLen = max(maxSeqLen, ctr) # check if this sequence is longer than the previously recorded sequence
     
     return maxSeqLen


print(longest_consecutive_sequence2([0,3,7,2,5,8,4,6,0,1]))





def group_anagrams(words):
     
     hashmap = {} # map the sorted version of a anagram to the the anagrams in the words array
     
     for i in range(len(words)):
          word = "".join(sorted(words[i]))
     
          if (word in hashmap):
               # append the regular version of the word rather than the sorted
               hashmap[word].append(words[i])
          else:
               hashmap[word] = [words[i]]
     
     final = []
     
     for i in hashmap.values():
          print(final.append(i))
          
     return final

print("this the one", group_anagrams(["eat","tea","tan","ate","nat","bat"]))



def valid_anagram(s, t):
     
     if len(s) != len(t):
          return False
     
     hashSetS = {}
     hashSetT = {}
     
     # same length so compare char by char for the same frequencies
     for i in range(len(s)):
          hashSetS[s[i]] = 1 + hashSetS.get(s[i], 0)
          hashSetT[t[i]] = 1 + hashSetT.get(t[i], 0)
     
     
     for j in hashSetT:
          if (hashSetS[j] != hashSetT.get(j, 0)):
               return False
     
     return True

print(valid_anagram("app", "pap"))

print("no")


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
     unique = list(set(nums))
     unique.sort()
     max_seq_len = 0
     for i in range(len(nums)):
          if (not nums[i]-1 in unique): # start of a new sequence
               curr_seq_len = 1
               while (nums[i]+curr_seq_len in unique): # start of a new sequence
                    curr_seq_len+=1
          max_seq_len = max(max_seq_len, curr_seq_len)
          
     return max_seq_len

print(longest_consecutive_sequence3([100, 4, 200, 1, 3, 2]))
          