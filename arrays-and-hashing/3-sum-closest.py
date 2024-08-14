class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if (sum < target):
                    j+=1
                else:
                    k-=1
                
                result = sum if abs(target - sum) < abs(target - result) else result
        return result   

        
# moving the pointer j up when sum is too small
# moving the pointer k down when sum is too large
# can't find the sum, then return the base case (result) because it's guaranteed there are at least 3 elements in list