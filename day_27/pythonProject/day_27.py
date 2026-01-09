import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(500, 500)

#label
my_label = tkinter.Label(text="I am a label", font=('Arial', 28, 'bold'))
my_label.pack()


#button
def ButtonClicked():
     new_text = inputs.get()
     my_label.config(text=f'{new_text}')

button = tkinter.Button(text='Click me!', command=ButtonClicked)
button.pack()

# Entry
inputs = tkinter.Entry(width=10)
inputs.pack()



window.mainloop()
