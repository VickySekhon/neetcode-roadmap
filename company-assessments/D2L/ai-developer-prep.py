# Rank the grades below (best to worst) 
# Example below should return: [2,2,2,1,5]
grades = [75,75,75,96,23]

mappings = {grade: indx for indx, grade in enumerate(set(grades),1)}

rankings = []
for i, grade in enumerate(grades, 1):
     rank = mappings[grade]
     rankings.append(rank)
     
print(rankings)