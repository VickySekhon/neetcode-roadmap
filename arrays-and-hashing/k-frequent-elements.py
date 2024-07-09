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
     arr = [[] for i in range(len(nums) + 1)]

     for i in nums:
          hashMap[i] = 1 + hashMap.get(i, 0)

     for n, c in hashMap.items():
          arr[c].append(n)
          
     result = []
     for i in range(len(arr) - 1, 0, -1):
          for n in arr[i]:
               if (len(result) != k):
                    result.append(n)
               
     return result

nums = [1,2,2,3,3,3]
k = 2
print(k_frequent_elements(nums,k))