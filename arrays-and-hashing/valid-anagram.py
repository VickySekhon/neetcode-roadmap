def validAnagram(s, t):
     """
     Checks if two strings, s and t, are anagrams of each other.

     An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
     In this case, we are checking if the characters in s can be rearranged to form t.

     Args:
          s (str): The first string.
          t (str): The second string.

     Returns:
          bool: True if s and t are anagrams, False otherwise.
     """
     if (len(s) != len(t)):
          return False

     hashSet = {}
     hashSet2 = {}

     for i in range(len(s)):
          
          hashSet[s[i]] = 1 + hashSet.get(s[i], 0)
          hashSet2[t[i]] = 1 + hashSet2.get(t[i], 0)
          
          
     for j in hashSet:
          if (hashSet[j] != hashSet2.get(j, 0)):
               return False
          
     return True

     # TODO: method 2
     return sorted(s) == sorted(t)

     # TODO: method 3
     
     arrS = list(s)
     
     for i in range(len(arrS)):
          min = i
          for j in range(i+1, len(arrS)):
               if (arrS[j] < arrS[min]):
                    min = j
          arrS[i], arrS[min] = arrS[min], arrS[i]
          
     
     arrT = list(t)
     
     for i in range(len(arrT)):
          min = i
          for j in range(i+1, len(arrT)):
               if (arrT[j] < arrT[min]):
                    min = j
          arrT[i], arrT[min] = arrT[min], arrT[i]
     
     
     return arrT == arrS

s = "cat"
t = "car"

print(validAnagram(s,t))



def validAnagram2(s, t):
     """
     Checks if two strings, s and t, are anagrams of each other.

     An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
     In this case, we are checking if the characters in s can be rearranged to form t.

     Args:
          s (str): The first string.
          t (str): The second string.

     Returns:
          bool: True if s and t are anagrams, False otherwise.
     """
     if len(s) != len(t):
          return False
     
     map1 = {} # s
     map2 = {} # t
     
     for i in range(len(s)):
          map1[s[i]] = 1 + map1.get(s[i], 0)
          map2[t[i]] = 1 + map2.get(t[i], 0)
     
     for i in map1:
          if map1[i] != map2.get(i, 0):
               return False
          
     return True
     
s = "catt"
t = "carr"

print(validAnagram2(s,t))

def valid_anagram(s1, s2):
     if s1 == "" and s2 == "":  return True
     
     s1_freq, s2_freq = {}, {}
     for letter1, letter2 in zip(s1, s2):
          s1_freq[letter1] = 1 + s1_freq.get(letter1, 0)
          s2_freq[letter2] = 1 + s2_freq.get(letter2, 0)
          # if not s1_freq.get(letter1):
          #      s1_freq[letter1] = 1
          # else:
          #      s1_freq[letter1] += 1
          # if not s2_freq.get(letter2):
          #      s2_freq[letter2] = 1
          # else:
          #      s2_freq[letter2] += 1
     
     return s1_freq.items() == s2_freq.items()

print(valid_anagram("cat", "tac"))