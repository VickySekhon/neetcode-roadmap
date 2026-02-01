
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

def search(nums: list[int], target: int) -> int:
     low, high = 0, len(nums)-1
     
     while low <= high:
          mid = (low+high)//2
          if nums[mid] == target:
               return mid
          if target > nums[mid]:
               low = mid+1
          else:
               high = mid-1
     
     return -1

nums = [-1,0,2,4,6,8]
target = 4
print(search(nums, target))