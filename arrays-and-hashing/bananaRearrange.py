def rearrange_bananas(encodedString):
     """
     Finds the # of times the word 'banana' can be spelt using 
     the characters in a string.

     Args:
          encodedString (str): Encoded string of random characters

     Returns:
          int: The # of times

     """
     hashTable = {}
     unique = "ABN"
     
     for char in encodedString:
          if char in unique:
               if char in hashTable:
                    hashTable[char] += 1
               else:
                    hashTable[char] = 1
                    
     times = 0
     while (hashTable.get('A',0)>=3 and
            hashTable.get('B',0)>=1 and
            hashTable.get('N',0)>=2):
          times+=1
          hashTable['A']-=3
          hashTable['B']-=1
          hashTable['N']-=2
     return times

print(rearrange_bananas("NANABXJSLWEFJSDBXNA")) # should return 1