"""
Missing element in large sorted array
"""
from random import randint
def missing_element(a):
     n = len(a)
     actual_sum = int((n*(n+1))/2) # sum of consecutive natural numbers up to n
     our_sum = sum(a)
     return actual_sum - our_sum

a = [i for i in range(1,100001)]
r = randint(0, 99999)
print("element missing: ", a[r])
a[r] = 0
x = missing_element(a)
print("the element we found to be missing: ", x)
     