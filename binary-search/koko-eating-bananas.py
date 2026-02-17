import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        ks = []
        for m in range(1, max(piles)+1):
            hours_taken = 0
            for n in piles:
                hours_taken += math.ceil(n/m)
            if hours_taken <= h: ks.append([m, hours_taken])
        k, _ = min(ks, key=lambda x : x[0])
        # print(ks)
        return k



def minEatingSpeed(piles: list[int], h: int) -> int:
     min_k = float('inf')
     l, r = 1, max(piles)
     while l <= r:
          print(l)
          m = (l+r)//2
          k = m
          hours = 0
          for pile in piles:
               hours += math.ceil(pile/k)
          print(f"hours taken by k={k}: {hours}\n")
          if hours > h: # I take longer than the hours, need to eat faster
               l = m+1
          elif hours <= h: # I take less time than the hours, am I the fastest?
               r = m-1
               if k < min_k:
                    min_k = k
               
     return min_k

piles=[312884470]
h=312884470
x = minEatingSpeed(piles, h)
print(x)