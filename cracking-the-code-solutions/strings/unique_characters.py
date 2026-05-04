def unique_characters(s):
     x = list("".join(s.split()))
     y = set(x)
     print(x, y)
     return len(x) == len(y)

def unique_characters_no_data_structures(s):
     for i in range(len(s)):
          char = s[i]
          for j in range(i+1, len(s)):
                next = s[j]
                if char == next:
                     return False 
     return True

non_unique = "hello"
unique = "paul"
print(unique_characters(non_unique))
print(unique_characters(unique))
print("----")
print(unique_characters_no_data_structures(non_unique))
print(unique_characters_no_data_structures(unique))