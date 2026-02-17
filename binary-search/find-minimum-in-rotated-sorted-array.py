class Solution:
     def findMin(self, nums: list[int]) -> int:
          nums.sort()
          return nums[0]


     def findMin2(self, nums: list[int]) -> int:
          l, r = 0, len(nums)-1
          if nums[r] < nums[l]: # array is rotated
               mid = 0
               while l < r:
                    mid = (l+r)//2
                    if nums[l] <= nums[mid]: # min is in the right
                         l = mid+1
                    elif nums[mid] < nums[r]: #  min is in the left
                         r = mid
          return nums[l]
     
sol = Solution()
# x = sol.findMin2([3,4,5,6,1,2])
# x = sol.findMin2([4,5,6,7])
x = sol.findMin2(nums=[3,4,5,1,2])
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