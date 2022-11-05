from tkinter import *


def open_file():
    print("File has been opened")


def save_file():
    print("File has been saved")


def cut():
    print("You cut some text")


def copy():
    print("You copied some text")


def paste():
    print("You pasted some text")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()
