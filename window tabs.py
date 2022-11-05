from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)   # widget that manages a collection of windows/displays

tab1 = Frame(notebook)   # new frame for tab1

tab2 = Frame(notebook)   # new frame for tab2

notebook.add(tab1, text="Tab1")
notebook.add(tab2, text="Tab2")
notebook.pack(expand=True, fill=BOTH)   # expand - this will expand to fill any space not otherwise used
# fill - this will fill empty space on x and y-axis

Label(tab1, text="Hello, you're currently on tab1", width=50, height=25).pack()
Label(tab2, text="Hello, you're currently on tab2", width=50, height=25).pack()

window.mainloop()
