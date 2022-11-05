from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo(title="info", message="This is info messagebox, click ok to close")
    messagebox.showwarning(title="warning", message="These settings may contain conflicts")
    messagebox.showerror(title="error", message="Something went wrong...")
    if messagebox.askyesno(title="ask yes or no", message="Do you want to apply changes?"):
        messagebox.showinfo(title="info", message="Changes successfully applied")
    else:
        messagebox.showinfo(title="info", message="Changes cancelled")
    if messagebox.askokcancel(title="ask ok cancel", message="Do you want to apply current settings?"):
        messagebox.showinfo(title="info", message="Applied settings settings successfully")
    else:
        messagebox.showinfo(title="info", message="Previous settings were loaded")
    messagebox.askyesnocancel(title="ask yes or no or cancel", message="Do you like to code?")   # this piece of code
    # make 3 statements: yes as True; no as False; cancel as None.


window = Tk()

button = Button(window, text="Click me", command=click)
button.pack()

window.mainloop()
