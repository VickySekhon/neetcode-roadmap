"""
Coding Interview Practice File

Instructions:
Implement the functions below so that all test cases pass.
Do NOT modify the test cases.
"""

############################################################
# Question 1
############################################################

"""
Given an array, count how many elements at index i are divisible
by the element at index i+1, where i+1 is a valid index.

Example:
[4,2,16,4] -> 2
4 % 2 == 0
2 % 16 != 0
16 % 4 == 0
"""


def divisible_count(nums):
    """
    TODO: Implement this function
    """
    count = 0
    for i in range(len(nums)-1):
        if nums[i] % nums[i + 1] == 0:
            count += 1
    return count


def test_divisible_count():
    print("Testing divisible_count...")

    assert divisible_count([4, 2, 16, 4]) == 2
    assert divisible_count([10, 5, 1]) == 2
    assert divisible_count([3, 6, 2]) == 1
    assert divisible_count([64, 32, 16, 8, 4]) == 4
    assert divisible_count([1]) == 0
    assert divisible_count([8, 4, 2, 1]) == 3

    print("divisible_count tests passed\n")


############################################################
# Question 2
############################################################

"""
Maximum Subarray Sum (Leetcode 53)

Given an integer array nums, find the contiguous subarray
(with at least one number) which has the largest sum.

Example:
nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Subarray: [4,-1,2,1]
"""


def max_subarray(nums):
    """
    TODO: Implement this function
    """
    window = 0
    max_window = float('-inf')
    
    for num in nums:
         window += num
         if window > max_window:
              max_window = window
         elif window < 0:
              window = 0
    
    return max_window


def test_max_subarray():
    print("Testing max_subarray...")

    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1, -2, -3]) == -1
    assert max_subarray([2, -1, 2, 3, 4, -5]) == 10

    print("max_subarray tests passed\n")


############################################################
# Question 3
############################################################

"""
Sort a singly linked list in ascending order.

Example:
Input: 5 -> 2 -> 6 -> 4 -> 9 -> 3
Output: 2 -> 3 -> 4 -> 5 -> 6 -> 9
"""


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            return

        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


def sort_linked_list(head):
    """
    TODO: Implement this function

    Input:
        head of linked list

    Output:
        head of sorted linked list
    """
    
    if not head or not head.next:
         return head

    left = head
    right = get_mid(left)
    tmp = right.next
    right.next = None
    right = tmp
    
    left = sort_linked_list(left)
    right = sort_linked_list(right)
    
    n_head = merge(left, right)
    return n_head

def get_mid(head):
     fast = head
     slow = head
     while fast and fast.next:
          fast = fast.next.next
          if not fast:
               break
          slow = slow.next
     return slow

def merge(left, right):
     new_node = Node()
     new_head = new_node # will be .next
     
     while left and right:
          if left.value <= right.value:
               new_node.next = left
               new_node = new_node.next
               left = left.next
          else:
               new_node.next = right
               new_node = new_node.next
               right = right.next
     if left:
          new_node.next = left
     elif right:
          new_node.next = right
     
     return new_head.next
 
def reverse_linked_list(head):
     prev = None
     curr = head
     while curr:
         _next = curr.next
         curr.next = prev
         prev = curr
         curr = _next
     self.head = prev
     return prev


def test_sort_linked_list():
    print("Testing sort_linked_list...")

    ll = LinkedList()
    for v in [5, 2, 6, 4, 9, 3]:
        ll.insert(v)

    ll.head = sort_linked_list(ll.head)
    assert ll.to_list() == [2, 3, 4, 5, 6, 9]

    ll = LinkedList()
    for v in [4, 1, 3, 2]:
        ll.insert(v)

    ll.head = sort_linked_list(ll.head)
    assert ll.to_list() == [1, 2, 3, 4]

    print("sort_linked_list tests passed\n")


############################################################
# Question 4
############################################################

"""
Missing element in large sorted array.

The array contains numbers from 1..n but one number is missing.

Example:
[1,2,3,4,6]
Output: 5
"""


def missing_element(nums):
    """
    TODO: Implement this function
    """
    n = len(nums)+1
    actual_sum = int((n*(n+1))/2)
    our_sum = sum(nums)
    return actual_sum - our_sum


def test_missing_element():
    print("Testing missing_element...")

    assert missing_element([1, 2, 3, 5]) == 4
    assert missing_element([1, 2, 4, 5]) == 3
    assert missing_element([2, 3, 4, 5]) == 1
    assert missing_element([1, 2, 3, 4, 5, 6, 8]) == 7

    print("missing_element tests passed\n")


############################################################
# Run All Tests
############################################################


def run_all_tests():
    test_divisible_count()
    test_max_subarray()
    test_sort_linked_list()
    test_missing_element()
    print("All tests passed!")


if __name__ == "__main__":
    run_all_tests()
