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