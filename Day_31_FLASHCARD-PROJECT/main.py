import tkinter
from tkinter import messagebox
import pandas
from random import choice
import json

BACKGROUND_COLOR = "#B1DDC6"
RIGHT_IMG = 'images/right.png'
WRONG_IMG = 'images/wrong.png'
FRONT_CARD_IMG = 'images/card_front.png'
LANG_FONT = ('Ariel', 40, 'italic')
BACK_CARD_IMG = 'images/card_back.png'
WORD_FONT = ('Ariel', 60, 'bold')
x = ''
y = ''
idk_words = {}
counter = 0

# -----------------------FUNCTIONS------------------------------------
def first_card():
    # Front Card
    # canvas.update()
    canvas.itemconfig(img, image=front_img)
    canvas.itemconfig(lang_text, fill='black', text='French', font=LANG_FONT)
    canvas.itemconfig(word_text, fill='black', text=rand_word['French'], font=WORD_FONT)
    # canvas.update()


def second_card():
    # Back Card
    # canvas.update()
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfig(lang_text, fill='white', text='English', font=LANG_FONT)
    canvas.itemconfig(word_text, fill='white', text=rand_word['English'], font=WORD_FONT)
    # canvas.update()


def right_button():
    global n_of_words, x, y, idk_words, wordlist
    window.after_cancel(x)
    window.after_cancel(y)
    index_of_word = wordlist.index(rand_word)
    wordlist.remove(wordlist[index_of_word])
    n_of_words = len(wordlist)
    flashcard_game()


def wrong_button():
    global x, y, idk_words, counter,wordlist
    # try:
    #     with open('wrong_words.json', 'r') as json_file:
    #         file_data = json.load(json_file)
    #         file_data.update(new_data)
    #     with open('wrong_words.json', 'w') as json_file:
    #         json.dump(file_data, json_file, indent=4)
    # except FileNotFoundError:
    #     with open('wrong_words.json', 'w') as json_file:
    #         json.dump(new_data, json_file, indent=4)
    #         lock = True
    window.after_cancel(x)
    window.after_cancel(y)
    counter+=1
    idk_words.update({f'{counter}':rand_word})
    index_of_word = wordlist.index(rand_word)
    wordlist.remove(wordlist[index_of_word])
    flashcard_game()


# -----------------------FILE READINGS--------------------------------
data = pandas.read_csv('data/french_words.csv')
wordlist = data.to_dict(orient='records')
n_of_words = len(wordlist)
rand_word = choice(wordlist)
# -------------------------UI SETUP----------------------------------
# WINDOW
window = tkinter.Tk()
window.title('FLASHY')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# BUTTONS

# Right Button
right_img = tkinter.PhotoImage(file=RIGHT_IMG)
r_button = tkinter.Button(image=right_img, highlightthickness=0, command=right_button)
r_button.grid(row=1, column=0)

# Wrong Button
wrong_img = tkinter.PhotoImage(file=WRONG_IMG)
w_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=wrong_button)
w_button.grid(row=1, column=1)

# CANVAS
canvas = tkinter.Canvas(width=800, height=526)
img = canvas.create_image(400, 263)
lang_text = canvas.create_text(400, 150, text='', font=LANG_FONT)
word_text = canvas.create_text(400, 263, text='', font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
front_img = tkinter.PhotoImage(file=FRONT_CARD_IMG)
back_img = tkinter.PhotoImage(file=BACK_CARD_IMG)


# -------------------------LOGIC SETUP----------------------------------


def flashcard_game():
    global rand_word, x, y
    if len(wordlist) > 0:
        rand_word = choice(wordlist)
        print(f'index of word:{wordlist.index(rand_word)}, word{rand_word}')
        x = window.after(0, func=first_card)
        y = window.after(3000, func=second_card)
    elif len(wordlist) == 0:
        tkinter.messagebox.showinfo(title="Oops", message="You have used up all the words")
        pandas.DataFrame(idk_words).to_csv('Words_to_learn.csv')
        # try:
        #     with open('wrong_words.json', 'r',encoding=) as json_file:
        #         file_data = json.load(json_file)
        #         file_data.update(idk_words)
        #     with open('wrong_words.json', 'r') as json_file:
        #         json.dump(file_data, json_file, indent=4)
        # except FileNotFoundError:
        #     with open('wrong_words.json', 'w') as json_file:
        #         json.dump(idk_words, json_file, indent=4)
        tkinter.messagebox.showinfo(title="END", message="The game has ended")
    # counter = 1
    # new_data = {f'Word {counter}': {'French': french_words[random], 'English': english_words[random]}}
    # counter+=1


flashcard_game()

window.mainloop()
