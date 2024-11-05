# Question 1
def find_odd_rows(data):
    odd_rows = []
    for i, row in enumerate(data):
        
        if all(value % 2 != 0 for value in row):
            odd_rows.append(row)  # Add the row itself or use i to save the row index
    return odd_rows

print(find_odd_rows(data))


# Question 2.1
def create_empty_board():
    checkerboard = [[0 for _ in range(8)] for _ in range(8)]
    return checkerboard

# Question 2.2
def create_checkerboard():
    checkerboard = [[0 for _ in range(8)] for _ in range(8)]
    
    for i in range(1, 8, 2):  
        checkerboard[i] = [1 if j % 2 == 0 else 0 for j in range(8)]
    
    return checkerboard


# Question 2.3
def create_checkerboard():
    checkerboard = [[0 for _ in range(8)] for _ in range(8)]
    
    for i in range(8):
        if i % 2 == 0: 
            checkerboard[i] = [0 if j % 2 == 0 else 1 for j in range(8)]
        else: 
            checkerboard[i] = [1 if j % 2 == 0 else 0 for j in range(8)]
    
    return checkerboard


# Question 2.4
def create_checkerboard():
    checkerboard = [[0 for _ in range(8)] for _ in range(8)]
    
    for i in range(8):
        if i % 2 == 0:  
            checkerboard[i] = [0 if j % 2 == 0 else 1 for j in range(8)]
        else:  
            checkerboard[i] = [1 if j % 2 == 0 else 0 for j in range(8)]
    
    return checkerboard


# Question 3

def expand_string(text, spaces):
    space_str = ' ' * spaces  
    expanded_text = space_str.join(text)  
    return expanded_text


# Question 4

import numpy as np

def second_largest_in_columns(arr):

    sorted_arr = np.sort(arr, axis=0)[::-1]    
    second_largest = sorted_arr[1]
    
    return second_largest

