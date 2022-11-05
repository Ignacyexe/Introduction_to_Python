from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", "*.*")
                                    ])
    if file is None:   # this line prevents from exceptions when exiting windows without any data
        return
    textfile = str(text.get(1.0, END))
    # textfile = input("Enter text: ")   # This code makes python console as text editor
    file.write(textfile)
    file.close()


def submit():
    enter = text.get("1.0", END)
    print(enter)


window = Tk()
window.title("Text editor")

text = Text(window,
            bg="light yellow",
            font=("Segoe Print", 16),
            height=8,
            width=20,
            padx=20,
            pady=20
            )
text.pack()

save = Button(window, text="Save", command=savefile)
save.pack(side=LEFT,
          padx=20,
          pady=3)

button = Button(window, text="Submit", command=submit)
button.pack(side=RIGHT,
            padx=20,
            pady=3)

window.mainloop()
