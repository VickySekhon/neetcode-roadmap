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
     
sol = Solution()
numbers = [-1,0,1,2,-1,-4]
#numbers = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(sol.threeSum(numbers))
# numbers = [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]


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
     
sol = Solution()
#numbers = [-1,0,1,2,-1,-4]
numbers = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(sol.threeSum(numbers))
# numbers = [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]
