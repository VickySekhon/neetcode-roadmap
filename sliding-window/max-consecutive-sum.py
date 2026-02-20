# def max_consecutive_sum(nums):
#      l, r = 0, 0
#      current_sum = 0
#      best_sum = -float('inf')
     
#      while l < len(nums):
#           current_sum = current_sum+nums[r]
#           if current_sum >= best_sum:
#                best_sum = current_sum
#           else:
#                current_sum = current_sum - nums[l]
#                if current_sum >= best_sum: best_sum = current_sum
#                l += 1
          
#           if r == len(nums)-1:
#                while l < r:
#                     summation = current_sum - nums[l]
#                     if summation > best_sum: best_sum = summation
#                     l += 1
#           else:
#                r+=1
               
     
#      return best_sum




def max_consecutive_sum(nums):
     current_sum = 0
     best_sum = -float('inf')
     
     for i in range(len(nums)):
          current_sum = current_sum+nums[i]

          if current_sum > best_sum: 
               best_sum = current_sum
          if current_sum < 0:
               current_sum = 0
     return best_sum

import unittest

class TestMaxConsecutiveSum(unittest.TestCase):
    def test_basic_mixed(self):
        """Max subarray is [5,3]"""
        self.assertEqual(max_consecutive_sum([10, -20, 5, 3, -4]), 10)

    def test_negative_in_middle(self):
        """Max subarray is [10,3,5]"""
        self.assertEqual(max_consecutive_sum([10, 3, 5, -30, 13, 2]), 18)

    def test_all_positive(self):
        """Entire array is the max subarray"""
        self.assertEqual(max_consecutive_sum([1, 2, 3, 4]), 10)

    def test_all_negative(self):
        """Least negative single element"""
        self.assertEqual(max_consecutive_sum([-3, -1, -4, -2]), -1)

    def test_single_element(self):
        self.assertEqual(max_consecutive_sum([5]), 5)

    def test_single_negative(self):
        self.assertEqual(max_consecutive_sum([-5]), -5)

    def test_large_negative_between_positives(self):
        """[5,4] or [5] — don't bridge over the -100"""
        self.assertEqual(max_consecutive_sum([5, -100, 4]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_consecutive_sum([-1, -2, 3, 4, 5]), 12)

    def test_max_at_start(self):
        self.assertEqual(max_consecutive_sum([5, 4, 3, -100, 1]), 12)

    def test_all_zeros(self):
        self.assertEqual(max_consecutive_sum([0, 0, 0, 0]), 0)

if __name__ == "__main__":
     #unittest.main()
     x = max_consecutive_sum([3, 6, -5, -9])
     print(x)