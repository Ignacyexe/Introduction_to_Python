from tkinter import *

window = Tk()
window.title("Input box 1.1")


def submit():
    username = entry.get()
    print("Hello " + username)
    submit_button.destroy()
    delete_button.destroy()
    checkbutton.destroy()
    label = None
    if not label:
        label = Label(window,
                      text=("Hello " + username + "!"),
                      font=("Constantia", 23),
                      compound=RIGHT,
                      )
    label.pack()


def delete():
    entry.delete(0, END)


def display():
    if x.get() == 1:
        submit()
    else:
        label_check = Label(window,
                            text="Please accept the terms and conditions",
                            fg="red",
                            compound=BOTTOM)
        window.after(1500, lambda: label_check.destroy())
        label_check.pack()


entry = Entry(window,
              font=("Constantia", 23))
entry.pack()

entry.insert(0, "Type your name")

submit_button = Button(window, text="submit", command=display, compound=RIGHT)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete, compound=RIGHT)
delete_button.pack(side=RIGHT)

x = IntVar()

checkbutton = Checkbutton(window,
                          text="I accept the terms and conditions",
                          compound="bottom",
                          variable=x,
                          command=display)
checkbutton.pack()

window.mainloop()
