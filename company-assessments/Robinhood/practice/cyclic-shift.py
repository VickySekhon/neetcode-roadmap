def cyclic_shift(elements):
     """ 
     Given elements array, return if elements "shifted"
     1 to n-1 positions from end to the beginning equals one
     of the identity arrays:
     
          1. [1,2,3, ... ,n]
          2. [n, n-1,...,2, 1]
     
     e.g. 
     elements = [1, 4, 2, 3], cyclic_shift(elements) should
     return False.
     
     moving 0 elements from the end gives: [1,4,2,3]
     moving 1 elements from the end gives: [3,1,4,2]
     moving 2 elements from the end gives: [2,3,1,4]
     moving 3 elements from the end gives: [4,2,3,1]
     
     None equals: [1,2,3,4], [4,3,2,1]
     """
     # n = len(elements)
     # identity = [i for i in range(1,n+1)]
     # identity_r = identity[::-1]
     
     # for _ in range(n):
     #      last_element = None
     #      for l in range(n):
     #           r = (l+1)%n
     #           if last_element:
     #                temp = elements[r]
     #                elements[r] = last_element
     #                last_element = temp
     #           else:     
     #                last_element = elements[r]
     #                elements[r] = elements[l]
          
     #      if elements == identity or elements == identity_r: return True
     #      print(elements)
     # return False
     
     identity = [i for i in range(1,len(elements)+1)]
     
     if len(identity) != len(elements):
          return False
     
     for i, valu in enumerate(identity):
          if valu == elements[0]:
               return identity[i:]+identity[:i] == elements
     
     return False

#x = cyclic_shift([1,4,2,3])
x = cyclic_shift([3,4,1,2])
                #[1,2,3,4]
print(x)