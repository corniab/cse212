# Looping through lists and the range function

"""
the range function has several properties
range(end)              - Select numbers from 0 to end-1
range(start, end)       - Select numbers from start to end-1
range(start, end, step) - Select numbers from start to end-1 stepping by step
"""

for i in range(5):
   print(i, end=" ")
# > 0
# > 1
# > 2
# > 3
# > 4

print()

for i in range(1,5):
     print(i, end=" ")
# > 1
# > 2
# > 3
# > 4

print()

for i in range(1,10,2):
     print(i, end=" ")
# > 1
# > 3
# > 5
# > 7 
# > 9
print()

"""
List comprehensions

my_list = [<expression> for <item> in <collection> if <condition>]
"""

my_list = [x for x in range(1, 5000, 133)]

print()
print()
print(my_list, sep=" ")
print()