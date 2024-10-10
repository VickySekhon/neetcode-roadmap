def maxWidthRamp(nums):
     """
     :type nums: List[int]
     :rtype: int
     """

     seq_lens = []

     for i in range(len(nums)):
          curr = nums[i]
          curr_seq_len = i
          for j in range(i+1, len(nums)):
               nxt = nums[j]
               if (curr <= nxt):
                    curr_seq_len = j
          seq_lens.append(curr_seq_len-i)
     
     return max(seq_lens)


print(maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))

print(maxWidthRamp([6,0,8,2,1,5]))