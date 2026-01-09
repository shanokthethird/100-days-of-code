import pandas

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random

# student_score = {students: random.randint(1, 100) for students in names}
# print(student_score)
# for (key, value) in student_score.items():
#     print(key)
#     print(value)
student_score = {'students': ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'],
                 'scores': [98,75,42,39,87,66]}
student_score_datafr = pandas.DataFrame(student_score)

# for (key, value) in student_score_datafr.items():
#     print(key)
# for (key, value) in student_score_datafr.items():
#     print(value)

for (index, row) in student_score_datafr.iterrows():
    if row.students == 'Alex':
        print(row.scores)