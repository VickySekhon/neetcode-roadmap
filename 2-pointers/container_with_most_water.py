
# O(n^2) brute force
def maxArea(heights):
     maximum = 0
     for i in range(len(heights)):
          for j in range(i + 1, len(heights)):
               x = j - i
               y = min(heights[i], heights[j])
               if (x * y > maximum):
                    maximum = x * y
     return maximum


print(maxArea([1,7,2,5,4,7,3,6])) 

def maxArea2(heights):
     l = 0
     r = len(heights)-1
     max_area = 0
     while l < r:
          x = r - l
          y = min(heights[l], heights[r])
          if (x * y > max_area):
               max_area = x*y
          
          l_smaller = heights[l] <= heights[r]
          if l_smaller:
               l += 1
          else:
               r -= 1
          
     return max_area

print(maxArea2([1,7,2,5,4,7,3,6])) 