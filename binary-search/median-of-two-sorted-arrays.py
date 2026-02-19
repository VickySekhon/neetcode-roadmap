import random, time, math, unittest
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # [1,2], [3]
        # [0,0], [0,0]

        # nums = [0] * (len(nums1)+len(nums2))
        # p, p_1, p_2 = 0, 0, 0
        # while p_1 < len(nums1) and p_2 < len(nums2):
        #     if nums1[p_1] <= nums2[p_2]:
        #         nums[p] = nums1[p_1]
        #         p_1 += 1
        #     elif nums2[p_2] < nums1[p_1]:
        #         nums[p] = nums2[p_2]
        #         p_2 += 1
        #     p += 1
        
        # if p_1 < len(nums1):
        #     while p < len(nums):
        #         nums[p] = nums1[p_1]
        #         p+=1
        #         p_1+=1
        # else:
        #     while p < len(nums):
        #         nums[p] = nums2[p_2]
        #         p+=1
        #         p_2+=1
        
        # mid = (len(nums)-1)//2
        # if len(nums) % 2 != 0: return nums[mid]
        # return (nums[mid] + nums[mid+1])/2
        
        # med = 0
        # if nums1[-1] > nums2[-1]:
        #     med = nums1[-1]
        # else:
        #     med = nums2[-1]
        # if (med/2) % 2 == 0:
        #     return ((med/2)+(med/2+1))/2
        # else:
        #     return math.ceil(med/2)
      
  
        # if len(nums1) == 0: return nums2[(len(nums2)-1)//2] if len(nums2)%2!=0 else (nums2[(len(nums2)-1)//2] + nums2[(len(nums2))//2])/2
        # if len(nums2) == 0: return nums1[(len(nums1)-1)//2] if len(nums1)%2!=0 else (nums1[(len(nums1)-1)//2] + nums1[(len(nums1))//2])/2
        
        l, r = 0, len(min(nums1, nums2, key=len))
        if len(nums1) > len(nums2):
          nums1, nums2 = nums2, nums1
        half = (len(nums1)+len(nums2))//2
        while l <= r:
          # partitions
          i = (l+r)//2
          j = half-i
          
          # Nothing on the left side
          if i <= 0:
            a_left_max = -float('inf')
          else:
            a_left_max = nums1[i-1]
          
          if j <= 0:
            b_left_max = -float('inf')
          else:
            b_left_max = nums2[j-1]
          
          # Nothing on the right side  
          if i == len(nums1):
            a_right_min = float('inf')
          else:
            a_right_min = nums1[i]
          
          if j == len(nums2):
            b_right_min = float('inf')
          else:
            b_right_min = nums2[j]
            
          
          print(f"a = [...{a_left_max}|{a_right_min}...]")
          print(f"b = [...{b_left_max}|{b_right_min}...]")
          
          if a_left_max <= b_right_min and b_left_max <= a_right_min:
            if (len(nums1) + len(nums2)) % 2 == 0: # even length, median is the average of the 
              median = (max(b_left_max, a_left_max) + min(b_right_min, a_right_min))/2
            else: # odd length, median is the middle element
              #median = max(b_left_max, a_left_max)
              median = min(b_right_min, a_right_min)
            return median
          else:
            if b_left_max > a_right_min:
              print(l, i, r)
              l = i+1
            else:
              r = i-1
        # l, r = 0, len(min(nums1, nums2, key=len))
        # if len(nums1) > len(nums2):
        #   nums1, nums2 = nums2, nums1
        # half = (len(nums1) + len(nums2))//2
        
        # while l <= r:
        #   mid_a = (l+r)//2
        #   mid_b = half - mid_a
          
        #   a_left_max = nums1[mid_a-1] if mid_a > 0 else -float('inf')
        #   a_right_min = nums1[mid_a] if mid_a != len(nums1) else float('inf') 
        #   b_left_max = nums2[mid_b-1] if mid_b > 0 else -float('inf')
        #   b_right_min = nums2[mid_b] if mid_b != len(nums2) else float('inf')

        #   if a_left_max <= b_right_min and b_left_max <= a_right_min:
        #     if (len(nums1) + len(nums2)) % 2 == 0:
        #       median = (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2
        #     else:
        #       median = min(a_right_min, b_right_min)
        #     return median
        #   else:
        #     if b_left_max > a_right_min:
        #       l = mid_a + 1
        #     else:
        #       r = mid_a - 1
        # return
class TestSum(unittest.TestCase):
    sol = Solution()
    def test1(self):
        """EVEN: [1,3] and [2,4]"""
        nums1 = [1,3]
        nums2 = [2,4]
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.5)
    def test2(self):
        """ODD: [1,4,6] and [2,5,7,9]"""
        nums1 = [1,4,6]
        nums2 = [2,5,7,9]
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 5)
    def test3(self):
        """EVEN: [0,0] and [0,0]"""
        nums1 = [0,0]
        nums2 = [0,0]
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 0)
    def test4(self):
        """ODD: [1,2] and [3]"""
        nums1 = [1,2]
        nums2 = [3]
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2)
    def test5(self):
        """EVEN: [1,3] and [2,4]"""
        nums1 = [1,3]
        nums2 = [2,4]
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.5)
    def test6(self):
        """EVEN: [1,2] and [3,4]"""
        nums1 = [1,2]
        nums2 = [3,4]
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.5)

if __name__ == "__main__":
    #unittest.main()
    #x = Solution().findMedianSortedArrays([1,2], [3])
    #x = Solution().findMedianSortedArrays([1,3], [2,4])
    #x = Solution().findMedianSortedArrays([1,2], [3,4])
    #x = Solution().findMedianSortedArrays(nums1=[], nums2=[1])
    nums1 = [random.randint(0,10**9) for i in range(10**7+1)]
    nums2 = [random.randint(0,10**9) for i in range(10**7+1)]
    # nums1 = [1,2,3]
    # nums2 = [4,5]
    start_time = time.perf_counter()
    x = Solution().findMedianSortedArrays(nums1, nums2)
    end_time = time.perf_counter()
    print(x)
    print(f"Execution time = {end_time-start_time:.2f}s")


    # x = sol.findMedianSortedArrays(nums1=[1,4,6], nums2=[2,5,7,9])
    # # x = sol.findMedianSortedArrays(nums1=[0,0], nums2=[0,0])

    # # x = sol.findMedianSortedArrays(nums1=[1,3,5,7,9], nums2=[2,4,6,8,10]) # 5.5
    # start_time = time.perf_counter()
    # #x = sol.findMedianSortedArrays(nums1, nums2)
    # end_time = time.perf_counter()
    # print(x)
    # print(f"Execution time = {end_time-start_time:.2f}s")