from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(initialdir="E:\\Ignacy\\Documents\\test.txt",
                                          title="Open file, okay?",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*"))  # we can choose
                                          # which type of file we want
                                          )
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()

button = Button(text="Open", command=openfile)
button.pack()

window.mainloop()
