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



class Solution2:
     # O(n^2 log (n))
     def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        temp = []
        seen = set()
        nums.sort() # O(n log (n))
        print(nums)
        for i in range(len(nums)):
             if i < len(nums) - 1 and nums[i] == nums[i+1]:
                  continue
             a, b = 0, 0
             indices = self.twoSumSorted(nums, -nums[i], i)
             if indices:
                  a, b = indices
                  temp.append(nums[i])
                  temp.append(nums[a])
                  temp.append(nums[b])
                  temp.sort()
                  if not tuple(temp) in seen: 
                      seen.add(tuple(temp))
                      res.append(temp[:])
                  temp = []
        return res
     
     # O(n)
     def twoSumSorted(self, nums, target, i):
          l = 0
          r = len(nums) - 1
          
          while l < r:
               if l == i:
                    l += 1
                    continue
               if r == i:
                    r -= 1
                    continue
               
               if nums[l] + nums[r] == target:
                    return l, r
               if nums[l] + nums[r] > target:
                    r -= 1
               else:
                    l += 1
          return None
     
sol2 = Solution2()
#numbers2 = [-1,0,1,2,-1,-4]
numbers2 = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(sol2.threeSum(numbers2))