from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question = Question
for questions in question_data:
    quest = questions['question']
    c_answer = questions['correct_answer']
    question_bank.append(question(quest, c_answer))
quiz = QuizBrain(question_bank)
quiz.next_question()
