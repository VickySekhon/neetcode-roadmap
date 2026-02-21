def pairs_with_power_of_two_sum(nums):
     """ 
     You’re given an array nums.
     You must count how many index pairs (i, j) satisfy:

     i ≤ j (so pairs can include the same element twice and order doesn’t matter)

     nums[i] + nums[j] is a power of 2

     e.g.
     
     nums = [1, 1, 3, 5]

     List all (i,j) with i ≤ j:

     (0,0): 1+1 = 2   ✅ power of 2
     (0,1): 1+1 = 2   ✅
     (0,2): 1+3 = 4   ✅
     (0,3): 1+5 = 6   ❌
     (1,1): 1+1 = 2   ✅
     (1,2): 1+3 = 4   ✅
     (1,3): 1+5 = 6   ❌
     (2,2): 3+3 = 6   ❌
     (2,3): 3+5 = 8   ✅
     (3,3): 5+5 = 10  ❌
     """
     return