from tkinter import messagebox
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FALSE_IMG = 'images/false.png'
TRUE_IMG = 'images/true.png'
FONT = ('Arial', 20, 'italic')
question_bank = []
MILLISECONDS = 100


class QuizWindow:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=10)
        self.score = Label(
            text=f'Score: {quiz_brain.score}/{quiz_brain.question_number}',
            bg=THEME_COLOR, fg='white',
            pady=20
        )
        self.score.grid(
            row=0,
            column=1
        )

        self.canvas = Canvas(
            width=300,
            height=250,
            bg='white',
        )
        self.text = self.canvas.create_text(
            150,
            125,
            text='#PLACEHOLDER',
            fill=THEME_COLOR,
            font=FONT,
            width=300
        )
        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=50)

        true_img = PhotoImage(file=TRUE_IMG)
        false_img = PhotoImage(file=FALSE_IMG)

        self.t_button = Button(
            image=true_img,
            highlightthickness=0,
            command=self.t_button,
            height=100,
            width=97
        )
        self.t_button.grid(
            row=2,
            column=0
        )
        self.f_button = Button(
            image=false_img,
            highlightthickness=0,
            command=self.f_button,
            height=100,
            width=97)
        self.f_button.grid(
            row=2,
            column=1
        )
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.question_number < len(self.quiz.question_list):
            q_text = self.quiz.next_question()
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.config(bg='white')
            self.t_button.config(state='disabled')
            self.f_button.config(state='disabled')
            self.canvas.itemconfig(self.text, text=f'GAME OVER\nYou have reached the end of the game, your score was '
                                                   f'{self.quiz.score}/{self.quiz.question_number}', anchor='center')

    def t_button(self):
        if self.quiz.check_answer('True'):
            self.canvas.config(bg='green')
            self.score_config()
            self.window.after(MILLISECONDS, func=self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.score_config()
            self.window.after(MILLISECONDS, func=self.get_next_question)

    def f_button(self):
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='green')
            self.score_config()
            self.window.after(MILLISECONDS, func=self.get_next_question)

        else:
            self.canvas.config(bg='red')
            self.score_config()
            self.window.after(MILLISECONDS, func=self.get_next_question)

    def score_config(self):
        self.score.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
