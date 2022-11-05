from tkinter import *


def create_window():
    # new_window = Toplevel()   # Toplevel() - new window on top of other windows, linked to a bottom window
    new_window = Tk()   # Tk() - new independent window
    window.destroy()    # close out old window


window = Tk()

Button(window, text="create new window", command=create_window).pack()

window.mainloop()
