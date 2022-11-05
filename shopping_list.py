from tkinter import *

window = Tk()
window.title("Shopping list")


def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    for i in food:
        label = Label(window,
                      text="You choose " + str(food) + " for shopping")
        label.pack()


def add():
    listbox.insert(listbox.size(), entryBox.get())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


listbox = Listbox(window,
                  font=("Monospace", 23),
                  selectmode=MULTIPLE)
listbox.pack()
listbox.config(height=listbox.size())
listbox.insert(1, "Bread")
listbox.insert(2, "Butter")
listbox.insert(3, "Eggs")
listbox.insert(4, "Cheese")
listbox.insert(5, "Snacks")
listbox.insert(6, "Milk")

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()

window.mainloop()
