def group_anagrams(words):
     """
     Groups a list of words into anagrams.

     Parameters:
     words (list): A list of strings representing words.

     Returns:
     list: A list of lists, where each inner list contains words that are anagrams of each other.
     """
     hashMap = {}
     result = []

     for i in words:
          sortedStr = "".join(sorted(i))
          if (not sortedStr in hashMap):
               hashMap[sortedStr] = [i]
          else:
               hashMap[sortedStr].append(i)

     # append all remaining values
     if hashMap.values():
          for j in hashMap.values():
               result.append(j)
          
     return result


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
