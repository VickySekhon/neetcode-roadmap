
def isPalindrome(s: str):

     s = "".join(s.split(" ")).lower()
     n_s = ""
     for char in s:
          if not char.isalpha() and not char.isnumeric():
               n_s += ""
          else:
               n_s += char
     
     l = 0
     r = len(n_s)-1
     while l < r:
          if n_s[l] != n_s[r]:
               return False
          l += 1
          r -= 1
     return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))