# check if string is palindrome recursively
# def is_palindrome(s):
#      if len(s) == 0 or len(s) == 1: return True
#      return palindrome_recur(s))

# def palindrome_recur(s, start, end):
#      if s[start] 
#           return True
     
#      palindrome_recur(s[])

# two pointers
def is_palindrome(s):
     lo, hi = 0, len(s)-1
     
     while lo < hi and s[lo] == s[hi]:
          lo += 1
          hi -= 1
     
     return lo >= hi # pointers intersect = all characters were equal

print(is_palindrome("dwerrewd"))

""" 
     string
        |
        V

     str ing
      |    |
      V    V
   st  r  in g
   
split string into half, palindrome_recur(first half) and palindrome_recur(second half)


     racecar
     
        |
      rac ecar
"""

def palindrome_recur(s, low, high):
     if low >= high:
          return True

     if s[low] != s[high]:
          return False
     
     return palindrome_recur(s, low+1, high-1)


print("recursive" , palindrome_recur("racecar", 0, 6))

# rank grades [2,2,2,1,5]
def rank_grades(grades):
     n = len(grades)
     mappings = {grade:[] for grade in grades}
     
     for i, grade in enumerate(grades):
          mappings[grade].append(i)
     
     print(mappings)
     
     grades = sorted(set(grades), reverse=True)
     print(grades)
     
     rank = 1
     rankings = [0 for i in range(n)]
     print(rankings)
     for grade in grades:
          indexes_to_update = mappings[grade]
          
          updates = rank
          for index in indexes_to_update:
               updates += 1
               rankings[index] = rank
          
          rank = updates
          
     return rankings
          
     
print(rank_grades([75,75,75,96,23])) # 96, 75, 23


# find day of week
