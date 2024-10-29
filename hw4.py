# Question 2.1
cute_dogs = list(range(21))

# Question 2.2
def square_elements(numbers):
    squared_numbers = [] 
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers

cute_dogs = list(range(21))

squared_numbers_0_to_20 = square_elements(numbers_0_to_20)

print("Squared numbers from 0 to 20:", squared_numbers_0_to_20)

# Question 2.3
def get_first_15_elements(numbers):
    return numbers[:15]
squared_numbers_0_to_20 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
# I intially used parantheses instead of brackets here, which gave me an error that I resolved by putting brackets around the numbers
first_15_squared_numbers = get_first_15_elements(squared_numbers_0_to_20)
print("First 15 elements of the squared list:", first_15_squared_numbers)


# Question 2.4
def get_every_5th_element(numbers):
    return numbers[4::5] 
squared_numbers_0_to_20 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
every_5th_squared_number = get_every_5th_element(squared_numbers_0_to_20)
print("Every 5th element of the squared list:", every_5th_squared_number)

# Question 2.5
def custom_slice_and_stride(numbers):
    last_30_elements = numbers[-30:]     
    every_3rd_in_reverse = last_30_elements[::-3]  
    return every_3rd_in_reverse

squared_numbers_0_to_20 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
result = custom_slice_and_stride(squared_numbers_0_to_20)

print("Every 3rd element of the last 30 elements in reverse:", result)


# Question 3.1
def create_5x5_matrix():
    matrix = []  
    count = 1    

    for i in range(5): 
        row = []  
        for j in range(5):  
            row.append(count)
            count += 1        
        matrix.append(row) 

    return matrix

sequential_5x5_matrix = create_5x5_matrix()

for row in sequential_5x5_matrix:
    print(row)


# Question 3.2
def create_5x5_matrix():
    matrix = []  
    count = 1    

    for i in range(5):  
        row = []  
        for j in range(5):  
            row.append(count)  
            count += 1        
        matrix.append(row)  

    return matrix

def replace_multiples_of_3(matrix):
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            if matrix[i][j] % 3 == 0: 
                matrix[i][j] = "?"  

sequential_5x5_matrix = create_5x5_matrix()

replace_multiples_of_3(sequential_5x5_matrix)

for row in sequential_5x5_matrix:
    print(row)


Question #3.3
def create_5x5_matrix():
    matrix = []  
    count = 1    

    for i in range(5):
        row = [] 
        for j in range(5):  
            row.append(count)  
            count += 1         
        matrix.append(row)

    return matrix

def sum_non_question_elements(matrix):
    total_sum = 0  
    for row in matrix:
        for element in row:
            if element != "?": 
                total_sum += element  
    return total_sum

sequential_5x5_matrix = create_5x5_matrix()
replace_multiples_of_3(sequential_5x5_matrix)

non_question_sum = sum_non_question_elements(sequential_5x5_matrix)

print("Sum of all non-'?' elements:", non_question_sum)
