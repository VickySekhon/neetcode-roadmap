# Technical Question Retry - Vicky Sekhon - 5:23pm May 22nd, 2025

# Rank the grades below (best to worst) 
# Example below should return: [2,2,2,1,5]
grades = [75,75,75,96,23]

# Initialize result array
result = [0 for i in range(len(grades))]

# For a given grade, track all the indexes
ht = {}
for i in range(len(grades)):
     if not grades[i] in ht.keys():
          ht[grades[i]] = [i]
     else:
          ht[grades[i]].append(i)
     
# Rankings begin with the largest grade first
grades.sort(reverse=True)
rank = 1

# Equivalent grades are given the same ranking so only need to focus on a single grade of any grade 
uniqueGrades = set(grades)

for grade in uniqueGrades:
     # Get all the locations of a grade
     indexes = ht[grade]
     
     # Track how many locations a single grade appears in
     updatedRank = rank
     for index in indexes:
          result[index] = rank
          updatedRank += 1

     # Start from the next appropriate ranking
     rank = updatedRank