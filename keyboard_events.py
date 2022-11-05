from tkinter import *


def do_something(event):
    # print("you pressed key " + event.keysym)
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>", do_something)

label = Label(window, font=("Helvetica", 75))
label.pack()

window.mainloop()
