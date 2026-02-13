# numbers = [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]

class Solution:
     # O(n^2 log (n))
     def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        temp = []
        
        nums.sort() # O(n log (n))
        print(nums)
        for i in range(len(nums)):
             a, b = 0, 0
             indices = self.twoSumSorted(nums, -nums[i], i)
             if indices:
                  a, b = indices
                  temp.append(nums[i])
                  temp.append(nums[a])
                  temp.append(nums[b])
                  temp.sort()
                  if not temp in res: res.append(temp)
                  temp = []
        return res
     
     # O(n)
     def twoSumSorted(self, nums, target, i):
          l = 0
          r = len(nums) - 1
          
          while l < r:
               while l == i and l < r:
                    l += 1
               while r == i and r > l:
                    r -= 1
               
               if nums[l] + nums[r] == target:
                    return l, r
               if nums[l] + nums[r] > target:
                    r -= 1
               else:
                    l += 1
          return None
     
# sol = Solution()
# numbers = [-1,0,1,2,-1,-4]
# #numbers = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# print(sol.threeSum(numbers))
# # numbers = [-1,0,1,2,-1,-4]
# # [-4, -1, -1, 0, 1, 2]


class Solution:
     # O(n^2 log (n))
     def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        nums.sort()
        
        for i, a in enumerate(nums):
             if a > 0:
                  break
             if i > 0 and nums[i] != nums[i-1]:
                  continue
             
             l = i + 1
             r = len(nums) - 1
             while l < r:
                  threeSum = nums[l] + nums[r] + a
                  if threeSum < a:
                       l += 1
                  elif threeSum > a:
                       r -= 1
                  else:
                       res.append([nums[l], nums[r], a])
                       l+=1
                       r-=1
                       while nums[l] == nums[l-1] and l < r:
                            l += 1
        return res
     
     # O(n)
     def twoSumSorted(self, nums, target, i):
          l = i+1
          r = len(nums) - 1
          
          while l < r:
               if nums[l] + nums[r] == target:
                    return l, r
               if nums[l] + nums[r] > target:
                    r -= 1
               else:
                    l += 1
          return None
     
# sol = Solution()
# #numbers = [-1,0,1,2,-1,-4]
# numbers = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# print(sol.threeSum(numbers))
# # numbers = [-1,0,1,2,-1,-4]
# # [-4, -1, -1, 0, 1, 2]

class Solution:
     def threeSum(self, nums):
          """ 
          input = [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
          """
          nums.sort()
          print(nums)
          triplets = []
          
          for i, num in enumerate(nums):
               values_we_need = self.twoSum(nums, -num, i, triplets)
               
               if values_we_need is None: continue
               
               num_2, num_3 = values_we_need
               pairing = sorted([num, num_2, num_3])
               
               if not pairing in triplets:
                    triplets.append(pairing)
               
               
          return triplets

     def representation(self, nums):
          return hash(tuple(sorted(nums)))
     

     def twoSum(self, nums, target, used_index, triplets):
          # if used_index == 7 or used_index == 8: print(nums, target)
          l, r = 0, len(nums)-1
          while l < r:
               # if used_index == 5:
               #      print(f"left: {nums[l]}, right: {nums[r]}, sum: {nums[l] + nums[r]}, target: {target}")
               if nums[l] + nums[r] == target and l != used_index and r != used_index:
                    #if used_index == 7 or used_index == 8: print([nums[l], nums[r]])
                    if sorted([-target, nums[l], nums[r]]) not in triplets:
                         return [nums[l],nums[r]]
               if nums[l] + nums[r] > target:
                    r -= 1
               else:
                    l += 1
          return


# sol = Solution()

# x = sol.threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49])
# print(x)

class Solution:
     def threeSum(self, nums):
          """ 
          input = [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
          
          [0, 0, 0, 0, 0, 1, 1, 2]
          """
          nums.sort()
          triplets = []
          
          for i, value in enumerate(nums):
               if i > 0 and nums[i] == nums[i-1]: continue
               
               l, r = i+1, len(nums)-1
               while l < r:
                    if value + nums[l] + nums[r] == 0:
                         triplets.append([value, nums[l], nums[r]])
                         l += 1
                         r -= 1
                         # found a combination x + l_pointer + value = 0 and x + r_pointer + value = 0
                         # cannot have that combination again and need to update both r and l pointers
                         while nums[l] == nums[l-1] and l < r:
                              l += 1
                         while nums[r] == nums[r+1] and l < r:
                              r -= 1
                    elif value + nums[l] + nums[r] > 0:
                         r -= 1
                    else:
                         l += 1
                         
          return triplets