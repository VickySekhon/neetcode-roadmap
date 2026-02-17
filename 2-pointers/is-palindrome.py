# Θ(n), Θ(n) space as well
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

# s = "A man, a plan, a canal: Panama"
# print(isPalindrome(s))


# Θ(n)
def isPalindrome(s: str):
     l = 0
     r = len(s)-1
     while l < r:
          while not s[l].isalnum() and l < r:
               l += 1
          while not s[r].isalnum() and r > l:
               r -= 1
          s_l = convertConstantLowercase(s[l])
          s_r = convertConstantLowercase(s[r])
          if s_l != s_r:
               return False
          l += 1
          r -= 1
     return True

def convertConstantLowercase(c: str):
     unicode = ord(c)
     if (unicode >= 65 and unicode <= 90):
          return chr(unicode + 32)
     
     return c

# s = "A man, a plan, a canal: Panama"
# print(isPalindrome(s))


class Solution(object):

    def isPalindrome(self, s):
        s = s.lower()
        new_s = ""
        for i in s:
             if i.isalnum(): new_s += i
        
        l, r = 0, len(new_s) - 1
        while l < r:
             if new_s[l] != new_s[r]: return False
             l += 1
             r -= 1
        
        return True

sol = Solution()
#x = sol.isPalindrome("A man, a plan, a canal: Panama")
x = sol.isPalindrome("0P")
print(x)