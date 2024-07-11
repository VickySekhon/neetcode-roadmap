from math import prod

def productExceptSelf(nums):
     """
     Calculates the product of array except self.

     Args:
          nums (int[]): The input array of integers.

     Returns:
          int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     # Implementation goes here
     result = []
     
     for i in range(len(nums)):
          leftArrProd = prod(nums[0:i])
          rightArrProd = prod(nums[i+1:len(nums)])
          result.append(leftArrProd * rightArrProd)

     return result

print(productExceptSelf([-1,0,1,2,3]))