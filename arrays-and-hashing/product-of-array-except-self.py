from math import prod

def productExceptSelf(nums):
     """
     Calculates the product of array except self.

     Args:
          nums (int[]): The input array of integers.

     Returns:
          int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     # TODO: creating left and right arrays and calculating the product using math library Prod()
     # TODO: PROBLEM: cannot use non-built in libraries in Python
     result = []
     
     for i in range(len(nums)):
          leftArrProd = prod(nums[0:i])
          rightArrProd = prod(nums[i+1:len(nums)])
          result.append(leftArrProd * rightArrProd)

     return result

print("FIRST: ", productExceptSelf([-1,0,1,2,3]))


def productExceptSelf2(nums):
     """
     Calculates the product of array except self.

     Args:
          nums (int[]): The input array of integers.

     Returns:
          int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     # TODO: appending a temporary array the different combinations of left and right arrays connected together, then performing multiplication of each array manually and appending the result into the final array
     # TODO: PROBLEM: O(n^2) time complexity due to nested for loop
     arr = []
     for i in range(len(nums)):
          leftArr = nums[0:i]
          rightArr = nums[i+1:len(nums)]
          arr.append(leftArr+rightArr)
     
     result = []
     for i in arr:
          product = 1
          for j in i:
               product *= j
          result.append(product)

     return result

print("SECOND: ", productExceptSelf2([-1,0,1,2,3]))

def productExceptSelf3(nums):
     """
     Calculates the product of array except self.

     Args:
          nums (int[]): The input array of integers.

     Returns:
          int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     # TODO: calculating total product and then dividing by each index
     # TODO: PROBLEM: cannot use division
     totalProd = 1
     
     for i in nums:
          totalProd *= i
     
     result = []
     for i in nums:
          temp = totalProd
          if (i != 0):
               temp //= i
          else:
               temp = 0
          result.append(temp)

     return result

print("THIRD: ", productExceptSelf2([-1,0,1,2,3]))


def productExceptSelf4(nums):
     """
     Calculates the product of array except self.

     Args:
          nums (int[]): The input array of integers.

     Returns:
          int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     # Implementation goes here
     prefix = [1] * len(nums)
     postfix = [1] * len(nums)
     
     # prefix
     for i in range(1, len(nums)):
          prefix[i] = prefix[i-1] * nums[i-1]
          
     # postfix
     for i in range(len(nums) - 2, -1, -1): # -1 because stop is not inclusive
          postfix[i] = postfix[i+1] * nums[i+1]
     
     result = []
     ctr = 0
     while ctr < len(prefix):
          result.append(postfix[ctr] * prefix[ctr])
          ctr += 1

     return result

print("**CORRECT**: ", productExceptSelf4([-1,0,1,2,3])) 



def productExceptSelf5(nums):
     """
     Calculates the product of array except self.

     Args:
     nums (int[]): The input array of integers.

     Returns:
     int[]: The output array where each element is the product of all elements in nums except the corresponding element.
     """
     prefix = [1] * len(nums)
     postfix = [1] * len(nums)
     
     
     for i in range(1, len(nums)):
          prefix[i] = prefix[i-1] * nums[i-1]
          
     for i in range(len(nums)-2, -1, -1):
          postfix[i] = postfix[i+1] * nums[i+1]
          
     i = 0
     result = [1] * len(nums)
     for i in range(len(postfix)):
          result[i] *= postfix[i] * prefix[i]
     
     return result

print(productExceptSelf5([-1,0,1,2,3]))