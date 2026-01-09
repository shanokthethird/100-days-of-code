import tkinter

KM_IN_A_MILE = 1.60934
#window
window = tkinter.Tk()
window.config(width=1000, height=1000)

#text
miles = tkinter.Label(text='Miles', font=('Arial', 20, 'bold'))
miles.grid(column=3, row=1)
is_equal = tkinter.Label(text='Is equal to', font=('Arial', 20, 'bold'))
is_equal.grid(column=1, row=2, )
num = tkinter.Label(text='0', font=('Arial', 20, 'bold'))
num.grid(column=2, row=2)
kmtxt = tkinter.Label(text='km', font=('Arial', 20, 'bold'))
kmtxt.grid(column=3, row=2)

#button
def ButtonClicked():
    value = inputs.get()
    num.config(text=f'{KM_IN_A_MILE * (float(value)):.2f}')


butt = tkinter.Button(text='Calculate!', command=ButtonClicked)
butt.grid(column=2, row=3)

#input
inputs = tkinter.Entry(width=10)
inputs.grid(column=2, row=1)

tkinter.mainloop()
