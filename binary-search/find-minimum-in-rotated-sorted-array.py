class Solution:
     def findMin(self, nums: list[int]) -> int:
          nums.sort()
          return nums[0]


     def findMin2(self, nums):
          l, r = 0, len(nums)-1
          
          while l < r:
               mid = (l+r)//2
               if nums[mid] > nums[r]: # array is shifted to the <--
                    l = mid + 1
               else: # array is shifted to the -->
                    r = mid
          return nums[r]

sol = Solution()
# x = sol.findMin2([3,4,5,6,1,2])
# x = sol.findMin2([4,5,6,7]) => [6,7,4,5] => [7,4,5,6]
#x = sol.findMin2(nums=[4,5,6,7,0,1,2 ])
x = sol.findMin2([5,1,2,3,4])
print(x)


""" 
[3,4,5,6,1,2]
 L   M     R
[3,4,5,6,1,2]
       L M R
[3,4,5,6,1,2]
       L R
       M
[3,4,5,6,1,2]
         R
         L
         M
[3,4,5,6,1,2]
         R
           L
         M
"""