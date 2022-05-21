"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def intersection(set1, set2):
    """
    Perform an intersection between 2 sets.  An intersection will contain
    the items in common between both sets.  Do not use the set 
    operators (+, -, *, &, |) and functions (intersection, union) 
    that are built-in to Python.
    """
    intersected = set()

    # Find the larger of the two sets.
    if len(set1) >= len(set2):
        larger = set1
        smaller = set2
    else:
        larger = set2
        smaller = set1

    for item in larger:
        if item in smaller:
            intersected.add(item)

    return intersected

def union(set1, set2):
    """
    Perform a union between 2 sets.  A union will contain all the items
    from both sets.   Do not use the set operators (+, -, *, &, |)
    and functions (intersection, union) that are built-in to Python.
    """
    united = set()
    for val in set1:
        united.add(val)

    for val in set2:
        united.add(val)

    return united

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(intersection(s1,s2))  # Should show {4, 5}
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8}

s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}
print(intersection(s1,s2))  # Should show an empty set
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Intersection of sets of different lengths
s1 = {1,2,3,4,5,6}
s2 = {1,2,3,4,5,6,10,12,13}
print(intersection(s1, s2)) # Should show {1,2,3,4,5,6}

