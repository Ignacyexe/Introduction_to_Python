from tkinter import *
from tkinter import colorchooser   # this is imported again because this is submodule


# noinspection PyTypeChecker
def click():
    color = colorchooser.askcolor()
    print(color)
    color_hex = color[1]
    print(color_hex)
    window.config(bg=color_hex)   # this line of code changes the background color of window
# this is more optimized version: window.config(colorchooser.askcolor()[1])


window = Tk()

window.geometry("420x420")
button = Button(text="choose color", command=click)
button.pack()

window.mainloop()
