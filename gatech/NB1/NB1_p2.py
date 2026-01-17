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
print(f'result={build_grade_dicts(grades)}')

# result= {'Thorny': {'Exam 1': 100, 'Exam 2': 90, 'Exam 3': 80},
#          'Mac': {'Exam 1': 88, 'Exam 2': 99, 'Exam 3': 111},
#          'Farva': {'Exam 1': 45, 'Exam 2': 56, 'Exam 3': 67},
#          'Rabbit': {'Exam 1': 59, 'Exam 2': 61, 'Exam 3': 67},
#          'Ursula': {'Exam 1': 73, 'Exam 2': 79, 'Exam 3': 83},
#          'Foster': {'Exam 1': 89, 'Exam 2': 97, 'Exam 3': 101}
#          }

