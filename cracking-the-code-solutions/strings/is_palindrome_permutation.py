def palindrome_permutation(s):
     s = "".join(s.split()).lower()
     freq_map = {}
     for char in s:
          if not freq_map.get(char):
               freq_map[char] = 1
          else:
               freq_map[char] += 1
     
     one_seen = False
     for k, v in freq_map.items():
          if v % 2 != 0:
               if v != 1:
                    return False
               
               if one_seen:
                    return False
                
               one_seen = True     
     print(s)
     print(freq_map)
     return True

print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("Nah bruh"))
print(palindrome_permutation("arce car"))