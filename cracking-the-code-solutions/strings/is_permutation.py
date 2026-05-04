def is_permutation_substring(s1, s2):
     s1, s2 = "".join(sorted(s1)), "".join(sorted(s2))
     c, i, j = 0, 0, 0
     while i < len(s1) and j < len(s2):
          if s1[i] == s2[j]:
               c += 1
               i += 1
               j += 1
          elif s1[i] > s2[j]:
               j += 1
          else:
               return False
               
     
     return c == len(s1)

# s1 = "ab"
# s2 = "eidbaooo"

# s1 = "abb"
# s2 = "eidbaaaabbooo"

s1 = "aaaab"
s2 = "eidbaaabbooo"
print(is_permutation_substring(s1, s2))


def is_permutation(s1, s2):
     return