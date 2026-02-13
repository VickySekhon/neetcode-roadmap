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
# sol = Solution()
# numbers = [1,2,3,4]
# target = 3
# print(sol.twoSum(numbers, target))
     
     
     
class Solution:
     def __init__(self) -> None:
          return
     
     def twoSum(self, numbers: list[int], target: int) -> list[int]:
          l = 0
          r = len(numbers) - 1
          triplets = []
          while l < r:
               if (numbers[l] + numbers[r] == target):
                    triplets.append([numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while numbers[l] == numbers[l-1] and l < r:
                         l += 1
                    while numbers[r] == numbers[r+1] and l < r:
                         r -= 1
               elif numbers[l] + numbers[r] > target:
                    r -= 1
               else:
                    l += 1
          return triplets
sol = Solution()
numbers = [0, 1, 2, 2, 3, 4, 4, 5, 6]
target = 6  # Can be solved by 2+4 (indices 2, 5 -> returns [3, 6])
print(sol.twoSum(numbers, target))
     