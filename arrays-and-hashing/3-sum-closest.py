def threeSumClosest(nums, target):
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

print(threeSumClosest([1,3,3,5,6], 5))


def threeSumClosest2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # i = base, j = one up from i, k = last element
    i = 0; j = 1; k = len(nums)-1
    
    result = nums[i]+nums[j]+nums[k]
    nums.sort()
    
    for i in range(len(nums)-2):
        j = i+1; k = len(nums)-1
        while (j < k):
            sum = nums[i]+nums[j]+nums[k]
            if sum > target:
                k-=1
            else:
                j+=1
            result = sum if abs(target - sum) < abs(target-result) else result
    
    return result
    
    
print(threeSumClosest2([1,3,3,5,6], 5))