# rank the grades below (should return: [2,2,2,1,5])
grades = [75,75,75,96,23]

res = [0 for i in range(len(grades))]
print(res)

ht = {}
for i in range(len(grades)):
     if not grades[i] in ht.keys():
          ht[grades[i]] = [i]
     else:
          ht[grades[i]].append(i)
     
grades.sort(reverse=True)

rank = 1

uniqueGrades = set(grades)

for grade in uniqueGrades:
     indexes = ht[grade]
     """ if len(indexes) > ) """
     
     print(indexes)
     updatedCount = rank
     for index in indexes:
          res[index] = rank
          updatedCount += 1

     rank = updatedCount

print(res)     
print(ht)