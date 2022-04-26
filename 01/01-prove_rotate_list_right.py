"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def rotate_list_right(data: list, amount: int):
    """
    Rotate the 'data' to the right by the 
    'amount'.   For example, if the data is 
    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount
    is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value 
    of amount will be in the range of 1 and 
    len(data).
    """
    for i in range(0, amount):
        # Get last array item.
        last = data[-1]

        # Shift the values right. Overwriting the last.
        data[1:] = data[0:-1]
        
        # Set the first value equal to the last
        data[0] = last
    return data

print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
