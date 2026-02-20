def max_subarray_size_k(nums, k):
     current_sum = sum(nums[:k])
     best_sum = current_sum
     
     j = 0
     for i in range(k, len(nums)):
          current_sum = current_sum+nums[i]-nums[j]
          if current_sum > best_sum: best_sum = current_sum
          j+=1
     
     # l, r = 0, k
     # while r < len(nums):
     #      current_sum = current_sum+nums[r]-nums[l]
     #      if current_sum > best_sum: best_sum = current_sum
     #      r+=1
     #      l+=1
     # return best_sum

import unittest

class TestMaxSubarraySizeK(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(max_subarray_size_k([1, 2, 3, 4], 2), 7)

    def test_k_equals_length(self):
        self.assertEqual(max_subarray_size_k([1, 2, 3, 4], 4), 10)

    def test_k_equals_one(self):
        self.assertEqual(max_subarray_size_k([3, 1, 4, 1, 5], 1), 5)

    def test_all_same(self):
        self.assertEqual(max_subarray_size_k([5, 5, 5, 5], 2), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_size_k([-1, -2, -3, -4], 2), -3)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_subarray_size_k([2, -1, 3, -2, 4], 3), 5)

    def test_max_at_start(self):
        self.assertEqual(max_subarray_size_k([9, 8, 1, 1, 1], 2), 17)

    def test_max_at_end(self):
        self.assertEqual(max_subarray_size_k([1, 1, 1, 8, 9], 2), 17)

    def test_single_element(self):
        self.assertEqual(max_subarray_size_k([42], 1), 42)

if __name__ == "__main__":
    unittest.main()