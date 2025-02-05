class Solution:
     def __init__(self) -> None:
          return
     
     def twoSum(self, numbers: list[int], target: int) -> list[int]:
          l = 0
          r = len(numbers) - 1
          
          while l < r:
               if (numbers[l] + numbers[r] == target):
                    return [l+1, r+1]
               if numbers[l] + numbers[r] > target:
                    r -= 1
               else:
                    l += 1
          return []
sol = Solution()
numbers = [1,2,3,4]
target = 3
print(sol.twoSum(numbers, target))
     