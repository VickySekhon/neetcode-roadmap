class Solution:
     def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        nums.sort() # O(n log (n))
        for i in range(len(nums)):
             a, b = 0, 0
             if (self.twoSumSorted(nums, -nums[i])):
                  a,b = self.twoSumSorted(nums, -nums[i])
             if a and b:     
               temp = []
               temp.append(nums[i])
               temp.append(nums[a])
               temp.append(nums[b])
               temp.sort()
               if not temp in res: res.append(temp)
               temp = []
             """              found = self.twoSumSorted(nums, -nums[i]) # O(n)
             
             if found is None:
                  continue
             temp = []
             temp.append(nums[i])
             temp.append(nums[found[0]])
             temp.append(nums[found[1]])
             temp.sort()
             if not temp in res: res.append(temp)
             temp = [] """
             
        return res
     
     def twoSumSorted(self, nums, target):
          l = 0
          r = len(nums) - 1
          
          while l < r:
               if nums[l] + nums[r] == target:
                    return l, r
               if nums[l] + nums[r] > target:
                    r -= 1
               else:
                    l += 1
          return
     
sol = Solution()
numbers = [-1,0,1,2,-1,-4]
print(sol.threeSum(numbers))