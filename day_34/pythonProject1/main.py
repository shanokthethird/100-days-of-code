from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizWindow
# import html
import translate as tr
#
# y_or_n = 'Yes'
# while y_or_n.upper() in ['Y', 'YES', 'T', 'TRUE']:
from data import question_data
question_bank = []
trans_q = tr.Translator('pt','en')

for questions in question_data:
    question_text = questions['question']
    question_answer = questions["correct_answer"]
    new_question = Question(trans_q.translate(question_text), question_answer)
    # new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizWindow(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
# y_or_n = input('Do you wish to continue?(y/n) ')
