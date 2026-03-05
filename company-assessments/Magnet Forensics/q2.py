"""
Max subarray Sum (Leetcode 53)
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # window = 0
        # max_window = float('-inf')
        
        # for i in nums:
        #   window = window + i
        #   if window > max_window:
        #     max_window = window
        #   if window < 0:
        #     window = 0
        
        # return max_window
        
        
        
        
        window = 0
        max_window = float('-inf')
        
        for num in nums:
          window += num
          if window > max_window:
            max_window = window
          if window < 0:
            window = 0
        
        return max_window

          
        
      
x = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(x))