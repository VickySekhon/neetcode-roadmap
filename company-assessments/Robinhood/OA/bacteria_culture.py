"""

You are given a line of bacteria, where each bacterium has:

a family name (a single letter) → from families

a size → from sizes

Both arrays are aligned:

families = ["A", "B", "C"]
sizes    = [ 5 ,  3 ,  7 ]

means: A(5)  B(3)  C(7)

Bacteria can eat other bacteria based on the following rules.

1️⃣ Only smaller bacteria can be eaten

A bacterium can eat another bacterium only if the target is smaller.

2️⃣ Only neighbors can be eaten

A bacterium can only eat adjacent bacteria:

the one to its left

the one to its right

3️⃣ Must be a different family

A bacterium cannot eat bacteria from the same family.

4️⃣ If two targets exist

If there are two smaller neighbors, the bacterium always eats the left one.

5️⃣ Eating effect

When a bacterium eats another:

its size increases by the size of the eaten bacterium

the eaten bacterium disappears from the line

Example:

A(5) B(3)

A eats B → A(8)

🔄 Simulation Process

The simulation happens in rounds.

Each round:

You scan from left → right

Bacteria eat if they can

The eaten bacterium is removed immediately

The process continues until no bacteria can eat another.

🎯 Final Goal

At the end, there will be one largest bacterium.

You must return:

"<family> <size>"

Example output:

"C 17"
"""

from typing import List

def solve(families: List[str], sizes: List[int]) -> str:
     eaten = True
     while eaten:
          eaten = False
          i = 0
          while len(families) > 1 and i < len(families):
               culture = families[i]
               size = sizes[i]
               
               if i == 0:
                    left = None
                    left_size = None 
                    right = families[i+1]
                    right_size = sizes[i+1]
               elif i == len(families)-1:
                    right = None
                    right_size = None
                    left = families[i-1]
                    left_size = sizes[i-1]
               else:
                    left = families[i-1]
                    left_size = sizes[i-1]
                    right = families[i+1]
                    right_size = sizes[i+1]
               
               if left is not None and culture != left and right is not None and culture != right:
                    # left needs to be removed
                    if (size > left_size and size > right_size) or size > left_size:
                         families.pop(i-1)
                         eaten_bacteria = sizes.pop(i-1)
                         i -= 1
                         sizes[i] += eaten_bacteria
                         eaten = True
                    # right needs to be removed
                    elif size > right_size:
                         families.pop(i+1)
                         eaten_bacteria = sizes.pop(i+1)
                         sizes[i] += eaten_bacteria 
                         eaten = True
               elif left and culture != left:
                    # left needs to be removed
                    if size > left_size:
                         families.pop(i-1)
                         eaten_bacteria = sizes.pop(i-1)
                         i -= 1
                         sizes[i] += eaten_bacteria
                         eaten = True
               elif right and culture != right:
                    # right needs to be removed
                    if size > right_size:
                         families.pop(i+1)
                         eaten_bacteria = sizes.pop(i+1)
                         sizes[i] += eaten_bacteria
                         eaten = True
               
               if not eaten:
                    i+=1
               
     max_culture_i = sizes.index(max(sizes))
     max_size = sizes[max_culture_i]
     max_culture = families[max_culture_i]
     return f"{max_culture} {max_size}"

x = solve(["green", "red", "blue", "yellow"], [5,6,7,5])
print(x)

def test_case_1():
    families = ["A", "B", "C", "D"]
    sizes = [5, 3, 7, 2]

    # Simulation:
    # A(5) B(3) C(7) D(2)

    # Round 1
    # A eats B -> A(8)
    # Line: A(8) C(7) D(2)

    # Continue scanning
    # A(8) eats C(7) -> A(15)
    # Line: A(15) D(2)

    # A(15) eats D(2) -> A(17)
    # Line: A(17)

    expected = "A 17"

    assert solve(families, sizes) == expected

test_case_1()

def test_case_2():
    families = ["A", "B", "A"]
    sizes = [4, 2, 3]

    # A(4) B(2) A(3)
    # A(4) eats B(2) -> A(6)
    # Line: A(6) A(3)
    # Same family → cannot eat

    expected = "A 6"
    assert solve(families, sizes) == expected


def test_case_3():
    families = ["A", "B", "C"]
    sizes = [2, 5, 3]

    # A(2) B(5) C(3)
    # B(5) eats A(2) -> B(7)
    # Line: B(7) C(3)
    # B(7) eats C(3) -> B(10)

    expected = "B 10"
    assert solve(families, sizes) == expected


def test_case_4():
    families = ["A", "B", "C", "D"]
    sizes = [3, 6, 2, 5]

    # A(3) B(6) C(2) D(5)

    # B(6) eats A(3) -> B(9)
    # Line: B(9) C(2) D(5)

    # B(9) eats C(2) -> B(11)
    # Line: B(11) D(5)

    # B(11) eats D(5) -> B(16)

    expected = "B 16"
    assert solve(families, sizes) == expected
    
    
def test_case_5():
    families = ["A", "B", "C"]
    sizes = [5, 2, 4]

    # A(5) B(2) C(4)
    # A eats B -> A(7)
    # A eats C -> A(11)

    expected = "A 11"
    assert solve(families, sizes) == expected


def test_case_6():
    families = ["A", "B", "C"]
    sizes = [2, 6, 3]

    # A(2) B(6) C(3)
    # B eats A -> B(8)
    # B eats C -> B(11)

    expected = "B 11"
    assert solve(families, sizes) == expected


def test_case_7():
    families = ["A", "A", "B"]
    sizes = [5, 3, 4]

    # A(5) A(3) B(4)
    # A cannot eat A
    # B eats A(3) -> B(7)
    # Line: A(5) B(7)
    # B eats A -> B(12)

    expected = "B 12"
    assert solve(families, sizes) == expected


def test_case_8():
    families = ["A", "B", "C", "A"]
    sizes = [3, 4, 2, 6]

    # A(3) B(4) C(2) A(6)
    # B eats A -> B(7)
    # Line: B(7) C(2) A(6)
    # B eats C -> B(9)
    # Line: B(9) A(6)
    # B eats A -> B(15)

    expected = "B 15"
    assert solve(families, sizes) == expected


def test_case_9():
    families = ["A", "B", "C", "D"]
    sizes = [1, 2, 3, 4]

    # A(1) B(2) C(3) D(4)
    # No bacterium has a smaller neighbor

    expected = "D 4"
    assert solve(families, sizes) == expected


def test_case_10():
    families = ["A", "B", "C", "B"]
    sizes = [5, 3, 4, 2]

    # A(5) B(3) C(4) B(2)
    # A eats B(3) -> A(8)
    # Line: A(8) C(4) B(2)
    # A eats C(4) -> A(12)
    # Line: A(12) B(2)
    # A eats B(2) -> A(14)

    expected = "A 14"
    assert solve(families, sizes) == expected
# def solve(families: List[str], sizes: List[int]) -> str:
#      eaten = True
#      while eaten:
#           eaten = False
#           new_families = []
#           new_sizes = []
#           for i, (culture, size) in enumerate(zip(families, sizes)):
#                if i == 0:
#                     left = None   
#                     right = families[i+1]
#                     right_size = sizes[i+1]
#                elif i == len(families)-1:
#                     right = None
#                     left = families[i-1]
#                     left_size = sizes[i-1]
#                else:
#                     left = families[i-1]
#                     left_size = sizes[i-1]
#                     right = families[i+1]
#                     right_size = sizes[i+1]
#                if left and culture != left and right and culture != right:
#                     if (size > left_size and size > right_size) or size > left:
#                          new_families.append(culture)
#                          new_sizes.append(size+left)
#                          eaten = True
#                     elif size > right:
#                          new_families.append(culture)
#                          new_sizes.append(size+right)
#                          eaten = True
#                elif left and culture != left:
#                     if size > left:
#                          new_families.append(culture)
#                          new_sizes.append(size+left)
#                          eaten = True
#                elif right and culture != right:
#                     if size > right:
#                          new_families.append(culture)
#                          new_sizes.append(size+right)
#                          eaten = True
               
#                if eaten:
#                     families = new_families
#                     sizes = new_sizes
               
#      max_culture_i = sizes.index(max(sizes))
#      max_size = sizes[max_culture_i]
#      max_culture = families[max_culture_i]
#      return f"{max_culture} {max_size}"

# TODO: couple problems: 1) inner for loop needs to be changed, since we need the updated families and sizes to immediately reflect, 2) i think if left and right are smaller, you will always eat left so first check is redundant, 3) compare sizes not left and right cultures

""" 
idea:

scan through each bacteria checking if a bacteria is a different culture from it's neighbor and can eat it's neighbor

     if culture is different from left and right:
          if it can eat left and right:
               - eat left (update size to size+left)
               - remove left from array
          if it can eat left:
               - eat left (update size to size+left)
               - remove left from array
          if it can eat right:
               - eat right (update size to size+right)
               - remove right from array
     elif culture is different from left:
          if it can eat left:
               - eat left (update size to size+left)
               - remove left from array
     elif culture is different from right:
          if it can eat right:
               - eat right (update size to size+right)
               - remove right from array
     
     check if anything was eaten in last simulation
     
     if so:
          run another simulation
     else:
          return largest size culture
          
pseudocode:

     eaten = True
     while eaten:
          eaten = False
          new_families = []
          new_sizes = []
          for i, (culture, size) in enum(zip(families, sizes)):
               if i == 0:
                    
               elif i == len(families)-1:
               
               left = families[i-1]
               right = families[i+1]
               if culture != left and culture != right:
                    if (size > left and size > right) or size > left:
                         new_families.append(culture)
                         new_sizes.append(size+left)
                         eaten = True
                    elif size > right:
                         new_families.append(culture)
                         new_sizes.append(size+right)
                         eaten = True
               elif culture != left:
                    if size > left:
                         new_families.append(culture)
                         new_sizes.append(size+left)
                         eaten = True
               elif culture != right:
                    if size > right:
                         new_families.append(culture)
                         new_sizes.append(size+right)
                         eaten = True
               
          families = new_families
          sizes = new_sizes
               
     max_culture_i = sizes.index(max(sizes))
     max_size = sizes[max_culture_i]
     max_culture = cultures[max_culture_i]
     return f"{max_culture} {max_size}"
"""