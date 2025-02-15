def trappingRainWater(heights):
     length = len(heights)
     total = 0
     i = 0
     
     visited = set()
     while i < length:
          l = heights[i]

          j = i+1

          raindrops = []
          
          while j < length and heights[j] < l:
               if not j in visited:
                    raindrops.append(heights[j])
               else:
                    visited[j] = 1
               j += 1
          print(raindrops)
          
          if j >= length:
               largest = max(raindrops)
               largest_i = raindrops.index(largest)
               t = 0
               while t < largest_i:
                    total += min(l, largest) - raindrops[t]
                    t+=1
          elif j < length and len(raindrops) > 0:
               r = heights[j]
               for drop in raindrops:
                    total += min(l, r) - drop
          else:
               j = i+1
          
          raindrops = []
          i = j
     
     return total

#print(trappingRainWater([0,2,0,3,1,0,1,3,2,1]))
print(trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trappingRainWater([4,2,3]))
print(trappingRainWater([6,8,5,0,0,6,5]))
