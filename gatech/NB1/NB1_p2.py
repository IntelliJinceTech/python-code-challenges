# 1.0.4  Exercise 3: (2 points)¶
#
# build_grade_dicts
#
# Your task: define build_grade_dicts as follows:
#
# Write a function that returns a dictionary of scores for each student.
#
# Inputs:
#
#     grades (list): a nested list of grades
#
# Return:
#
#     grade_dicts (dict): a nested dictionary
#         key is a student
#         value is another dictionary
#             key is the assignment
#             value is the score as an integer
#
# Nested dict that uses different combinations of the first row of data as the keys to the rest of the nested list
table = [
    ["ID", "Color", "Size", "Quantity"],  # Row 0: Headers
    ["A1", "Red", "Large", 10],  # Row 1: Data
    ["A1", "Blue", "Small", 5],  # Row 2: Data
    ["B2", "Green", "Medium", 8]  # Row 3: Data
]

# 1. Separate the headers from the data
headers = table[0]
data_rows = table[1:]

# 2. Identify your "Main Key" (e.g., the ID at index 0)
main_dict = {}

for row in data_rows:
    # Use the first item as the top-level key
    record_id = row[0]

    if record_id not in main_dict:
        main_dict[record_id] = []  # Using a list because one ID might have many entries

    # 3. Create a dictionary for the "Rest" using the Headers
    # We skip index 0 because that's our main key
    details = {}
    for i in range(1, len(headers)):
        header_name = headers[i]
        value = row[i]
        details[header_name] = value

    main_dict[record_id].append(details)


def build_grade_dicts(grades:list) -> dict:
    result = {}
    headers = grades[0]
    grade_data = grades[1:]

    for row in grade_data:
        student_name = row[0]

        exam_grades = {}
        for ind in range(1,len(row)):
            header_name = headers[ind] # e.g. exam 1 label
            grade_value = int(row[ind]) # e.g. exam 1 grade
            exam_grades[header_name] = grade_value # creating key, value pair for each label and grade
        result[student_name] = exam_grades # combining student(key) and the nested grades(value) together
    return result

# grades = [
# First line is descriptive header. Subsequent lines hold data
# ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
# ['Thorny', '100', '90', '80'],
# ['Mac', '88', '99', '111'],
# ['Farva', '45', '56', '67'],
# ['Rabbit', '59', '61', '67'],
# ['Ursula', '73', '79', '83'],
# ['Foster', '89', '97', '101']
# ]
# print(f'result={build_grade_dicts(grades)}')

# result= {'Thorny': {'Exam 1': 100, 'Exam 2': 90, 'Exam 3': 80},
#          'Mac': {'Exam 1': 88, 'Exam 2': 99, 'Exam 3': 111},
#          'Farva': {'Exam 1': 45, 'Exam 2': 56, 'Exam 3': 67},
#          'Rabbit': {'Exam 1': 59, 'Exam 2': 61, 'Exam 3': 67},
#          'Ursula': {'Exam 1': 73, 'Exam 2': 79, 'Exam 3': 83},
#          'Foster': {'Exam 1': 89, 'Exam 2': 97, 'Exam 3': 101}
#          }

#  Exercise 5: (2 points)
#
# build_grade_by_asn
#
# Your task: define build_grade_by_asn as follows:
#
# Write a function that returns a dictionary of scores for each assignment.
#
# Inputs:
#
#     grades (list): a nested list of grades
#
# Return:
#
#     grades_by_assignment (dict): a dictionary
#         key is an assignment
#         value is a list of scores with the scores converted to integers
#
# Hint:
#
#     You may find earlier exercises useful for completing this exercise.


### Solution - Exercise 5
def build_grade_by_asn(grades: list) -> dict:
    ###
    ### YOUR CODE HERE
    ###

    # initialize a new dict
    # initialize lists for each exam?
    # separate the header from the grade data
    # separate the student header from the exams headers
    # loop over each row
    #   loop over each exam in the row
    #     if index is for exam 1,2,3 - append to corresponding list
    exam_headers = grades[0][1:]
    exams = [[] for _ in exam_headers]  # list comprehension for adding dynamic empty lists
    data = grades[1:]

    for row in data:
        for i, val in enumerate(row[1:]):
            exams[i].append(int(val))
    asn_grades = dict(zip(exam_headers,exams))
    return asn_grades




### Demo function call
grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]
# print(f'result={build_grade_by_asn(grades)}')

# should be
# result={'Exam 1': [100, 88, 45, 59, 73, 89], 'Exam 2': [90, 99, 56, 61, 79, 97], 'Exam 3': [80, 111, 67, 67, 83, 101]}

# Exercise 6
# build_avg_by_asn
# Your task: define build_avg_by_asn as follows:
# Write a function that returns a dictionary of average scores for each assignment.
#
# Inputs:
#     grades (list): a nested list of grades
# Return:
#     avg_assignment (dict): a dictionary
#         key is an assignment
#         value is an average grade for that assignment rounded to 3 decimal places

### Solution - Exercise 6
def build_avg_by_asn(grades: list) -> dict:
    ###
    ### YOUR CODE HERE
    ###
# import statistics
    from statistics import mean
# separate exam-related headers from the rest of the headers and data
    exam_headers = grades[0][1:]
    data = grades[1:]

# create dynamic empty lists for each of the exams/assignments - assign it to a variable
    exams = [[] for _ in exam_headers]
# iterate over rows in the data portion
    for row in data:
        for ind,val in enumerate(row[1:]):
#   add value into the empty lists
            exams[ind].append(int(val))
    # print(exams)
# take rounded avg of the values in the empty lists
    rounded_avg = [round(mean(num),3) for num in exams]
# assign to dictionary with the exam headers (zip?)
    avg_dict = dict(zip(exam_headers,rounded_avg))
    return avg_dict



### Demo function call
grades = [
# First line is descriptive header. Subsequent lines hold data
['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
['Thorny', '100', '90', '80'],
['Mac', '88', '99', '111'],
['Farva', '45', '56', '67'],
['Rabbit', '59', '61', '67'],
['Ursula', '73', '79', '83'],
['Foster', '89', '97', '101']
]
# print(f'result={build_avg_by_asn(grades)}')

# The demo should display this printed output.
#
# result={'Exam 1': 75.667, 'Exam 2': 80.333, 'Exam 3': 84.833}


# 1.0.8  Exercise 7: (2 points)
#
# get_ranked_students
#
# Your task: define get_ranked_students as follows:
#
# Write a function that returns a list of sorted students.
#
# Inputs:
#
#     grades (list): a nested list of grades
#
# Return:
#
#     ranked_students (list): a list containing students ordered by:
#         average score descending order
#         break any ties by name in ascending alphabetical order
#
# Hint:
#
#     You may find earlier exercises useful for completing this exercise.
#     ranked_students[0] would be the student with the highest average exam score while ranked_students[-1] would have the lowest average exam score.


# 1.0.8  Exercise 7: (2 points)
#
# get_ranked_students
#
# Your task: define get_ranked_students as follows:
#
# Write a function that returns a list of sorted students.
#
# Inputs:
#
#     grades (list): a nested list of grades
#
# Return:
#
#     ranked_students (list): a list containing students ordered by:
#         average score descending order
#         break any ties by name in ascending alphabetical order
#
# Hint:
#
#     You may find earlier exercises useful for completing this exercise.
#     ranked_students[0] would be the student with the highest average exam score while ranked_students[-1] would have the lowest average exam score.

# The demo should display this printed output.

### Solution - Exercise 7
def get_ranked_students(grades: list) -> list:
    ###
    ### YOUR CODE HERE
    ###
#   import statistics/mean
    from statistics import mean
# create dictionary for each student as the key, avg score as the value
    student_dict = {}
    student_grades = grades[1:]
    for rows in student_grades:
        student = rows[0]
        stu_grades = mean([int(num) for num in rows[1:]])
        student_dict[student] = stu_grades
# sort dictionary
#   1. from highest to lowest avg score
    sorted_dict = sorted(student_dict.items(),key=lambda x:(-x[1],x[0]))
#   2. alphbetical from a - z
# return the list of keys of the dictionary
    return list(dict(sorted_dict).keys())

### Demo function call
grades = [
# First line is descriptive header. Subsequent lines hold data
['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
['Thorny', '100', '90', '80'],
['Mac', '88', '99', '111'],
['Farva', '45', '56', '67'],
['Rabbit', '59', '61', '67'],
['Ursula', '73', '79', '83'],
['Foster', '89', '97', '101'],
['Abigail', '99', '99', '100']
]
print(f'result={get_ranked_students(grades)}')

# result=['Abigail', 'Mac', 'Foster', 'Thorny', 'Ursula', 'Rabbit', 'Farva']
