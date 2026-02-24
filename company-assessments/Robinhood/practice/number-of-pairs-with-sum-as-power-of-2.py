import math
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
     # pairs = 0
     # for i in range(len(nums)):
     #      for j in range(i, len(nums)):
     #           pair_sum = nums[i] + nums[j]
               
     #           while pair_sum > 1:
     #                pair_sum /= 2
               
     #           if pair_sum == 1:
     #                pairs += 1
     # return pairs
     
     freq = {}
     for num in nums:
          if freq.get(num):
               freq[num] += 1
          else:
               freq[num] = 1
     
     pows = []
     _max = max(nums) * 2
     highest_pow = math.floor(math.sqrt(_max))
     for i in range(highest_pow+1):
          pows.append(2**i)

     print(freq, pows)
     pairs = 0
     for a in freq:
          for p in pows:
               b = p-a
               if b not in freq:
                    continue
               if a != b and b>a:
                    pairs += freq[a]*freq[b]
               elif a == b:
                    pairs += int((freq[a]*(freq[a]+1))/2)
                    
     return pairs
x = pairs_with_power_of_two_sum([1,1,3,5])
print(x)


"""
[1,1,3,8,8]

8 + 8 = 16

{1: 2, 3: 1, 8: 2}
pows = 1,2,4,8,16

p-a = b
(1) if b is in map and not equal to a, then if b > a then add it (prevent duplicates)
(2) if b is in map and equal to a

1-1=0 not in map
2-1=1 in the map, add pairing to the pairs

"""