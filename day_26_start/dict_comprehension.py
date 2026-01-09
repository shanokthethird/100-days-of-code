# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random

student_score = {students: random.randint(1, 100) for students in names}
print(student_score)

passed_students = {students: 'passed' for (students, score) in student_score.items() if score > 60}
print(passed_students)
