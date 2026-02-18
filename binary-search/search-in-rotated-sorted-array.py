class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        partition_1 = self.binary_search(nums, target, 0, l-1)
        partition_2 = self.binary_search(nums, target, l, len(nums)-1)
        if partition_1 != -1:
            return partition_1
        return partition_2
            
            
    def binary_search(self, nums, target, l, r):
        print(l, r)
        while l <= r:
            print(nums)
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
   
sol = Solution()
nums=[1,2,3,4,5,6]
target=7
x = sol.search(nums, target)
print(x)