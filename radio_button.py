from tkinter import *

food = ["Coca Cola", "Pepsi", "Dr. Pepper"]

window = Tk()

label = Label(window, text="What do you want to drink?", font=("Constantia", 14))
label.pack(side=BOTTOM)


def choose():
    global label
    if x.get() == 0:
        label.config(text="You choose Coca Cola!")
    if x.get() == 1:
        label.config(text="You choose Pepsi!")
    if x.get() == 2:
        label.config(text="You choose Dr. Pepper")


x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],   # adds text to radio buttons
                              variable=x,   # groups the radio buttons together if they share the same variable
                              value=i,   # assigns each radiobutton a different value
                              padx=15,
                              font=("Liberation serif", 13),
                              command=choose,
                              width=20
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
